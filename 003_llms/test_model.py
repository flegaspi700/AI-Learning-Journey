import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Load the base model and tokenizer
base_model_id = "meta-llama/Llama-2-7b-hf"
base_tokenizer = AutoTokenizer.from_pretrained(base_model_id)
base_model = AutoModelForCausalLM.from_pretrained(base_model_id, device_map="auto")

# 2. Load the fine-tuned model
fine_tuned_model_path = "./fine-tuned-llama"
fine_tuned_model = AutoModelForCausalLM.from_pretrained(fine_tuned_model_path, device_map="auto")

# 3. Define a prompt
prompt = "What is the capital of France?"

# 4. Generate response from base model
base_model_input = base_tokenizer(prompt, return_tensors="pt").to("cuda")
base_model_output = base_model.generate(**base_model_input, max_new_tokens=50)
base_model_response = base_tokenizer.decode(base_model_output[0], skip_special_tokens=True)

# 5. Generate response from fine-tuned model
fine_tuned_model_input = base_tokenizer(prompt, return_tensors="pt").to("cuda")
fine_tuned_model_output = fine_tuned_model.generate(**fine_tuned_model_input, max_new_tokens=50)
fine_tuned_model_response = base_tokenizer.decode(fine_tuned_model_output[0], skip_special_tokens=True)

# 6. Print the responses
print("--- Base Model Response ---")
print(base_model_response)
print("\n--- Fine-Tuned Model Response ---")
print(fine_tuned_model_response)
