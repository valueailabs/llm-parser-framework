# src/llms/coheremodel.py
import os
from langchain_community.llms import Cohere
from src.llms.llm_base import LLMBase

class CohereModel(LLMBase):
    def __init__(self, model_name: str):
        self.model_name = model_name.replace("cohere-", "")
        # model_name will be command-r now.
        os.environ["COHERE_API_KEY"] = "your-cohere-api-key"
        self.llm = Cohere(model=self.model_name, temperature=0.7)
