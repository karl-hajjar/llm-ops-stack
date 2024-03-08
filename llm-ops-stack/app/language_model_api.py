import logging
import os
import json

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.messages import SystemMessage

logger = logging.getLogger()


class LanguageModelAPI:
    """
    A class defining an API with:
    * an app attribute that runs a Flask app able to deal with requests (text queries)
    * an llm attribute to deal with usual text queries
    * an embeddings model which can be used for document retrieval
    """
    N_MAX_PROMPTS = 100
    SYSTEM_MESSAGE = "Your are a helpful and harmless AI assistant."

    def __init__(self, llm_model_name: str = "llama2"):
        self.llm_model_name = llm_model_name
        self.prompts_queue = []

        self._set_llm()
        self._set_embeddings_model()

    def _set_llm(self):
        """
        Sets the llm as Llama2 loaded from Ollama (https://ollama.com/). This could be changed in the future and a
        parameter could be passed to the __init__ method with the name or instantiation of the desired llm to be used in
        the API. The API to call the llm is defined through langchain
        (https://python.langchain.com/docs/get_started/introduction).

        The llm is initialized with a system message telling it to be a helpful and harmless assistant.
        :return:
        """
        self.llm = Ollama(model=self.llm_model_name)
        initial_messages = [SystemMessage(content=self.SYSTEM_MESSAGE)]
        self.llm.invoke(initial_messages)

    def _set_embeddings_model(self):
        """
        Sets the text embdeding model as Llama2 loaded from OllamaEmbeddings. This could be changed in the future and a
        parameter could be passed to the __init__ method with the name or instantiation of the desired llm to be used in
        for embedding text. The API to call the embedding model is defined through langchain.
        :return:
        """
        self.embedding_model = OllamaEmbeddings(model=self.llm_model_name)

    def update_prompts_queue(self, prompt: str):
        if len(self.prompts_queue) < self.N_MAX_PROMPTS:
            self.prompts_queue.append(prompt)



