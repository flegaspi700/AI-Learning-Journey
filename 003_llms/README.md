# LLM Fine-Tuning Project

This project provides a set of scripts and data to demonstrate the process of fine-tuning a Large Language Model (LLM) using Parameter-Efficient Fine-Tuning (PEFT), specifically with LoRA (Low-Rank Adaptation).

The project uses the Hugging Face `transformers`, `peft`, and `trl` libraries to fine-tune a Llama 2 model on a custom dataset.

> **Note:** This is a project for testing and learning how to fine-tune a Large Language Model.

## File Structure

- `fine_tuning.py`: The main script to run the fine-tuning process. It loads a base model, applies a LoRA configuration, and trains the model on the data in `data/dataset.json`.
- `evaluate_model.py`: A script to evaluate the performance of the fine-tuned model using the `data/evaluation_dataset.json`.
- `test_model.py`: A script to compare the outputs of the base model and the fine-tuned model for a given prompt.
- `llm_finetuning_guide.md`: A detailed guide explaining the concepts and steps involved in fine-tuning an LLM.
- `data/`:
    - `dataset.json`: The dataset used for fine-tuning the model.
    - `evaluation_dataset.json`: The dataset used for evaluating the model's performance.


