# src/extractor/main_module.py
import os
from src.llms.llm_factory import LLMFactory
from src.extractor.logger import log

"""
extract one attribute from the input test using the given model
"""
def main(input_text: str, attribute_name: str, model_name: str):
    prompt = load_prompt(attribute_name)
    llm_instance = LLMFactory.get_llm(model_name)
    response = llm_instance.get_response(input_text=input_text, prompt=prompt)
    log.info(f"Response: {response}")
    return response

def load_prompt(attribute_name: str) -> str:
    prompt_file = f"prompts/{attribute_name}.txt"
    if not os.path.exists(prompt_file):
        raise ValueError(f"Prompt file for attribute '{attribute_name}' not found.")
    
    with open(prompt_file, 'r') as file:
        prompt = file.read().strip()
    
    return prompt
