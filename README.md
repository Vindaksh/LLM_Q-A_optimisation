# LLM_Q-A_optimisation
Training an LLM to respond to Q and A type queries.
This code contains:  
a)Prompts to be used on LLM  
b)Additions to append to the prompts  
c)Paragraphs, Questions related to the paragraph and expected answers.    

The exact text sent to the LLM would be :

Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation.  
Paragraph: Electric vehicles (EVs) are becoming increasingly popular due to climate concerns. They use electric motors powered by batteries.  
Question: Why are EVs becoming popular?  
Answer:  

We do 3 iterations of prompts, with each iteration appending an addition.  
After 3 iterations we see that the correctness score increases after appending various additions to every prompt.
The output by the 3rd iteration lists the prompts with its additions along with correctness scores after iterations.  
This concept is similar to Deep reinforcement Learning where we train the model to suit our requirements .    

Example output:  
--- Iteration 1 ---

Prompt performance:  
→ 0.503: Using only the given paragraph, respond accurately.  
→ 0.296: Answer the question based on the paragraph only.  
→ 0.255: Read the paragraph carefully and provide a concise answer.  
  
--- Iteration 2 ---

Prompt performance:  
→ 0.582: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation.  
→ 0.566: Answer the question based on the paragraph only. Please give a step-by-step explanation.  
→ 0.547: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph.  
→ 0.450: Using only the given paragraph, respond accurately. Keep your response short and factual.  
→ 0.432: Answer the question based on the paragraph only. Keep your response short and factual.  
→ 0.415: Using only the given paragraph, respond accurately. Please give a step-by-step explanation.  
→ 0.388: Answer the question based on the paragraph only. Respond in one clear sentence.  
→ 0.387: Read the paragraph carefully and provide a concise answer. Keep your response short and factual.  
→ 0.380: Answer the question based on the paragraph only. Make sure your answer is based strictly on the paragraph.  
→ 0.377: Using only the given paragraph, respond accurately. Respond in one clear sentence.  
→ 0.356: Read the paragraph carefully and provide a concise answer. Explain the reasoning briefly.  
→ 0.345: Answer the question based on the paragraph only. Explain the reasoning briefly.  
→ 0.338: Read the paragraph carefully and provide a concise answer. Make sure your answer is based strictly on the paragraph.    
→ 0.324: Using only the given paragraph, respond accurately. Explain the reasoning briefly.  
→ 0.322: Read the paragraph carefully and provide a concise answer. Respond in one clear sentence.  

--- Iteration 3 ---

Prompt performance:  
→ 0.691: Answer the question based on the paragraph only. Please give a step-by-step explanation. Keep your response short and factual.  
→ 0.667: Answer the question based on the paragraph only. Please give a step-by-step explanation. Explain the reasoning briefly.  
→ 0.612: Answer the question based on the paragraph only. Please give a step-by-step explanation. Make sure your answer is based strictly on the paragraph.  
→ 0.503: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph. Please give a step-by-step explanation.  
→ 0.484: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation. Explain the reasoning briefly.  
→ 0.463: Answer the question based on the paragraph only. Please give a step-by-step explanation. Please give a step-by-step explanation.  
→ 0.442: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation. Respond in one clear sentence.  
→ 0.435: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation. Make sure your answer is based strictly on the paragraph.  
→ 0.435: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph. Explain the reasoning briefly.  
→ 0.429: Answer the question based on the paragraph only. Please give a step-by-step explanation. Respond in one clear sentence.  
→ 0.407: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph. Keep your response short and factual.  
→ 0.379: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation. Keep your response short and factual.  
→ 0.357: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph. Respond in one clear sentence.  
→ 0.266: Using only the given paragraph, respond accurately. Make sure your answer is based strictly on the paragraph. Make sure your answer is based strictly on the paragraph.  
→ 0.239: Read the paragraph carefully and provide a concise answer. Please give a step-by-step explanation. Please give a step-by-step explanation.  

