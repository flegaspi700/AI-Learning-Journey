# Import necessary libraries
# torch is a popular deep learning framework.
import torch
# load_dataset is used to easily load datasets from various sources.
from datasets import load_dataset
# These are from the Hugging Face transformers library, used for loading pre-trained models and tokenizers.
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
# PEFT (Parameter-Efficient Fine-Tuning) helps in fine-tuning large models efficiently.
# LoraConfig is for configuring LoRA, and get_peft_model applies it to a model.
from peft import LoraConfig, get_peft_model
# SFTTrainer is a specialized trainer for supervised fine-tuning from the TRL (Transformer Reinforcement Learning) library.
from trl import SFTTrainer

# --- 1. Load the Dataset ---
# We're loading a dataset from a JSON file.
# 'data_files' points to the location of our training data.
# 'split="train"' specifies that we are loading the training part of the dataset.
dataset = load_dataset("json", data_files="D:\\Learn\\AI-Learning\\AI-Learning-Journey\\003_llms\\data\\dataset.json", split="train")

# --- 2. Load the Model and Tokenizer ---
# We specify the pre-trained model we want to use. "meta-llama/Llama-2-7b-hf" is a 7-billion parameter Llama 2 model.
model_id = "meta-llama/Llama-2-7b-hf"
# The tokenizer is responsible for converting text into a format the model can understand (tokens).
# We load the tokenizer that corresponds to our chosen model.
tokenizer = AutoTokenizer.from_pretrained(model_id)
# We load the actual pre-trained model.
# 'device_map="auto"' automatically places the model parts on the best available devices (e.g., GPU, CPU).
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# --- 3. Configure LoRA (Low-Rank Adaptation) ---
# LoRA is a technique to fine-tune large models with much less memory and computational cost.
# It works by adding small, trainable "adapter" layers instead of training the entire model.
lora_config = LoraConfig(
    r=16,  # The "rank" of the LoRA matrices. A higher rank means more trainable parameters. 16 is a common choice.
    lora_alpha=32,  # A scaling factor for the LoRA updates.
    # We specify which parts of the model to apply LoRA to. "q_proj" and "v_proj" are parts of the attention mechanism.
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,  # Dropout helps prevent overfitting.
    bias="none",  # Specifies how to handle bias terms. "none" is a common setting.
    task_type="CAUSAL_LM"  # Specifies the type of task. Causal Language Modeling is for predicting the next word.
)

# --- 4. Add LoRA to the Model ---
# This function wraps our base model with the LoRA configuration, making it ready for efficient fine-tuning.
model = get_peft_model(model, lora_config)

# --- 5. Configure Training Arguments ---
# These arguments control the training process.
training_args = TrainingArguments(
    output_dir="./results",  # Where to save training outputs (like checkpoints).
    per_device_train_batch_size=4,  # How many training examples to process on each device (GPU) at once.
    gradient_accumulation_steps=4,  # Simulates a larger batch size by accumulating gradients over several steps.
    learning_rate=2e-4,  # The speed at which the model learns.
    logging_steps=10,  # How often to log training progress.
    max_steps=100  # The total number of training steps to perform.
)

# --- 6. Create the Trainer ---
# The SFTTrainer makes it easy to train models for tasks like instruction following or question answering.
trainer = SFTTrainer(
    model=model,  # The model we're training.
    train_dataset=dataset,  # The dataset to train on.
    dataset_text_field="prompt",  # The name of the column in our dataset that contains the input text.
    peft_config=lora_config,  # The PEFT configuration we defined earlier.
    args=training_args,  # The training arguments.
    max_seq_length=1024,  # The maximum length of the input sequences.
)

# --- 7. Start Training ---
# This command starts the fine-tuning process.
trainer.train()

# --- 8. Save the Model ---
# After training, we save the fine-tuned LoRA adapter layers (not the whole model).
# This creates a small file that can be loaded later to apply the fine-tuning to the original Llama 2 model.
trainer.save_model("./fine-tuned-llama")