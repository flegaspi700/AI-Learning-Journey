
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Load the fine-tuned model and tokenizer
fine_tuned_model_path = "./fine-tuned-llama"
# It's important to load the tokenizer from the fine-tuned model's directory if it was saved there
tokenizer = AutoTokenizer.from_pretrained(fine_tuned_model_path)
model = AutoModelForCausalLM.from_pretrained(fine_tuned_model_path, device_map="auto")

# 2. Load the evaluation dataset
evaluation_dataset = load_dataset("json", data_files="evaluation_dataset.json", split="train")

def get_prediction(prompt):
    """
    This is a simplified prediction function.
    In a real-world scenario, you would want to have a more robust way
    to extract the classification from the model's output.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=10)
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Simple extraction of the first word of the completion
    # This part is highly dependent on how your model formats its output
    try:
        prediction = decoded_output.split()[-1].lower().replace('.', '')
    except IndexError:
        prediction = ""
    return prediction

correct_predictions = 0
total_predictions = len(evaluation_dataset)

for example in evaluation_dataset:
    prompt = example["prompt"]
    ground_truth = example["completion"]
    
    prediction = get_prediction(prompt)
    
    print(f"Prompt: {prompt}")
    print(f"Prediction: {prediction}")
    print(f"Ground Truth: {ground_truth}")
    print("-" * 20)
    
    if prediction == ground_truth:
        correct_predictions += 1

if total_predictions > 0:
    accuracy = (correct_predictions / total_predictions) * 100
    print(f"\nAccuracy: {accuracy:.2f}%")
else:
    print("No data found in the evaluation dataset.")
