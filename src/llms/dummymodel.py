# src/llms/llama2model.py
from src.llms.llm_base import LLMBase

class DummyModel(LLMBase):
    """
    Do nothing dumy model to test the rest of the framework code
    """
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.llm = dummy_get_response

def dummy_get_response(input: str) -> str:
    return "dummy_value"
        
