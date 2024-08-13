# src/llms/llm_factory.py
from src.llms.gptmodel import GPTModel
from src.llms.coheremodel import CohereModel
from src.llms.dummymodel import DummyModel

class LLMFactory:
    """
    This class creates and returns the right LLM object.
    """
    @staticmethod
    def get_llm(model_name: str):
        if model_name == "gpt-3.5-turbo":
            return GPTModel(model_name)
        elif model_name == "cohere-command-r":
            return CohereModel(model_name)
        elif model_name == "dummy":
            return DummyModel(model_name)
        else:
            raise ValueError(f"Unsupported model: {model_name}")