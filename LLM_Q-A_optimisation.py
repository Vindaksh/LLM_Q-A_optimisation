# QA_optimization_with_mutation.py
# Optimizing LLM question answering prompts using a reinforcement-like loop.

import random
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Example dataset
dataset = [
    {
        "paragraph": (
            "The Amazon rainforest, often called the lungs of the Earth, produces 20 percent of the worlds oxygen and is home to millions of species. Deforestation caused by agriculture and logging threatens its biodiversity."
        ),
        "questions": [
            {"question": "Why is the Amazon rainforest important?", 
             "answer": "It produces oxygen and supports millions of species."},
            {"question": "What threatens the Amazon rainforest?", 
             "answer": "Deforestation from agriculture and logging."}
        ]
    },
    {
        "paragraph": (
            "The internet revolutionized communication by connecting people across the world. It enabled instant information sharing and created new industries such as e-commerce and social media."
        ),
        "questions": [
            {"question": "How did the internet change communication?",
             "answer": "It allowed instant information sharing globally."},
            {"question": "Name two industries that arose from the internet.",
             "answer": "E-commerce and social media."}
        ]
    },
    {
        "paragraph": (
            "Electric vehicles (EVs) are becoming increasingly popular due to concerns over climate change. They use electric motors powered by batteries instead of internal combustion engines."
        ),
        "questions": [
            {"question": "Why are electric vehicles becoming popular?",
             "answer": "Because of environmental and climate change concerns."},
            {"question": "How are EVs powered?",
             "answer": "They use batteries and electric motors."}
        ]
    }
]

# Base prompts
prompt_variations = [
    "Answer the question based on the paragraph only.",
    "Read the paragraph carefully and provide a concise answer.",
    "Using only the given paragraph, respond accurately.",
]

# Helper functions

def ask_llm(paragraph, question, prompt):
    """Generate answer using Hugging Face model."""
    input_text = f"{prompt}\n\nParagraph: {paragraph}\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
            temperature=0.7,  # encourage variation
            do_sample=True,   # non-deterministic sampling
            num_return_sequences=1
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()


def evaluate_answer(pred, actual):
    """Simple lexical similarity reward (can replace with semantic metric later)."""
    pred_words = set(pred.lower().split())
    actual_words = set(actual.lower().split())
    if not actual_words:
        return 0
    return len(pred_words & actual_words) / len(actual_words)


def mutate_prompt(prompt):
    """
    Generate multiple mutated prompts for one base prompt,
    each with exactly one addition.
    """
    additions = [
        " Please give a step-by-step explanation.",
        " Keep your response short and factual.",
        " Make sure your answer is based strictly on the paragraph.",
        " Respond in one clear sentence.",
        " Explain the reasoning briefly."
    ]
    return [prompt + add for add in additions]



# Optimization loop
def optimize_prompts(dataset, prompt_variations, iterations=3, top_k=3):
    for iteration in range(iterations):
        print(f"\n--- Iteration {iteration + 1} ---")

        prompt_scores = {prompt: 0 for prompt in prompt_variations}

        # Evaluate every prompt on every paragraph
        for data in dataset:
            paragraph = data["paragraph"]

            for prompt in prompt_variations:
                total_reward = 0
                for q in data["questions"]:
                    pred = ask_llm(paragraph, q["question"], prompt)
                    reward = evaluate_answer(pred, q["answer"])
                    total_reward += reward

                avg_reward = total_reward / len(data["questions"])
                prompt_scores[prompt] += avg_reward  # accumulate score

        # Compute overall averages
        num_paragraphs = len(dataset)
        prompt_avg_scores = {p: s / num_paragraphs for p, s in prompt_scores.items()}

        # Sort prompts by average reward
        sorted_prompts = sorted(prompt_avg_scores.items(), key=lambda x: x[1], reverse=True)

        print("\nPrompt performance:")
        for prompt, score in sorted_prompts:
            print(f"→ {score:.3f}: {prompt}")

        # Keep top_k best prompts and mutate them for next iteration
        best_prompts = [p for p, _ in sorted_prompts[:top_k]]
        mutated_prompts = [mutate_prompt(p) for p in best_prompts]

        # new
        mutated_prompts = []
        for p in best_prompts:
            mutated_prompts.extend(mutate_prompt(p))  # adds every addition individually

        # remove duplicates
        prompt_variations = list(dict.fromkeys(mutated_prompts))

    return prompt_variations


# Run optimization
best_prompts_found = optimize_prompts(dataset, prompt_variations, iterations=3)

#after 3 iterations we see that the correctness score increases after appending various additions to every prompt.
#the output by the 3rd iteration lists the prompts with its additions along with correctness scores after iterations.
#this concept is similar to Deep reinforcement Learning where we train the model to suit our requirements
