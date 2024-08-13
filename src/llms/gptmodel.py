# src/llms/gptmodel.py
import os
from langchain_community.llms import OpenAI
from src.llms.llm_base import LLMBase

class GPTModel(LLMBase):
    def __init__(self, model_name: str):
        self.model_name = model_name
        os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
        self.llm = OpenAI(model_name=self.model_name, temperature=0.7)
    
