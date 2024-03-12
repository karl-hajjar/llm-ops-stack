import logging
import os

from langchain_community.llms import LlamaCpp
from langchain_core.messages import SystemMessage

from sentence_transformers import SentenceTransformer

ROOT = os.path.dirname(os.path.dirname(__file__))  # llm-ops-stack root for python code
logger = logging.getLogger()


class LanguageModelAPI:
    """
    A class defining an API with:
    * an app attribute that runs a Flask app able to deal with requests (text queries)
    * an llm attribute to deal with usual text queries
    * an embeddings model which can be used for document retrieval
    """
    SYSTEM_MESSAGE = "Your are a helpful and harmless AI assistant."

    def __init__(self, llm_model_file: str = "llama-2-7b-chat.Q4_K_M.gguf"):
        self.llm_model_file = llm_model_file
        self.llm_model_path = os.path.join(os.path.dirname(ROOT), self.llm_model_file)

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
        self.llm = LlamaCpp(model_path=self.llm_model_path, temperature=0)  # deterministic output
        initial_messages = [SystemMessage(content=self.SYSTEM_MESSAGE)]
        self.llm.invoke(initial_messages)

    def _set_embeddings_model(self):
        """
        Sets the text embedding model as Llama2 loaded from OllamaEmbeddings. This could be changed in the future and a
        parameter could be passed to the __init__ method with the name or instantiation of the desired llm to be used in
        for embedding text. The API to call the embedding model is defined through langchain.
        :return:
        """
        self.embedding_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


