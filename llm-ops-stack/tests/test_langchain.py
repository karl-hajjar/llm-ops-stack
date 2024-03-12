import unittest
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain

from langchain_community.llms import Ollama, LlamaCpp
from langchain_community.embeddings import OllamaEmbeddings, LlamaCppEmbeddings


ROOT = os.path.dirname(os.path.dirname(__file__))


class TestLangChain(unittest.TestCase):
    def setUp(self) -> None:
        self.llama2_cpp_path = os.path.join(os.path.dirname(ROOT), "llama-2-7b-chat.Q4_K_M.gguf")

    def test_llama2_cpp(self):
        llm = LlamaCpp(model_path=self.llama2_cpp_path, temperature=0)
        system_message = "Your are a helpful and harmless AI assistant."
        messages = [SystemMessage(content=system_message)]
        llm.invoke(messages)
        result = llm.invoke("What is the capital of France ?")
        result = llm.invoke("Hi, what is 2+3 ?")
        self.assertTrue(True)

    def test_llama2_cpp_embeddings(self):
        embedding_model = LlamaCppEmbeddings(model_path=self.llama2_cpp_path)
        query = "What is the capital of France ?"
        vector = embedding_model.embed_query(query)
        self.assertTrue(True)

    def test_hf_sentence_embedding(self):
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        sentence = ['This framework generates embeddings for each input sentence']
        embedding = model.encode(sentence)
        self.assertTrue(True)

    def test_ollama_llm(self):
        llm = Ollama(model="llama2")
        system_message = "Your are a helpful and harmless AI assistant."
        messages = [SystemMessage(content=system_message)]
        llm.invoke(messages)
        result = llm.invoke("What is the capital of France ?")
        result = llm.invoke("Hi, what is 2+3 ?")
        self.assertTrue(True)

    def test_llama2_small_llm(self):
        llm = Ollama(model="llama2:7b")
        system_message = "Your are a helpful and harmless AI assistant."
        messages = [SystemMessage(content=system_message)]
        llm.invoke(messages)
        result = llm.invoke([HumanMessage("What is the capital of France ?")])
        result = llm.invoke([HumanMessage("Hi, what is 2+3 ?")])
        self.assertTrue(True)

    def test_ollama_chat(self):
        system_message = "Your are a helpful and harmless AI assistant."
        messages = [SystemMessage(content=system_message)]
        chat_llm = ChatOllama(model="llama2", temperature=0)
        result = chat_llm.invoke("What is the capital of France ?")
        self.assertTrue(True)

    def test_ollama_chain(self):
        llm = Ollama(model="llama2")
        chain = ConversationChain(llm=llm, verbose=False, memory=ConversationBufferMemory())
        system_message = "Your are a helpful and harmless AI assistant."
        messages = [SystemMessage(content=system_message)]
        chain.invoke(messages)
        result = chain.predict(input="Hi, what is 2+3 ?")
        result = chain.predict(input="What if I add 5 to the result ?")
        self.assertTrue(True)

    def test_ollama_embeddings(self):
        embedding_model = OllamaEmbeddings(model="llama2")
        query = "What is the capital of France ?"
        vector = embedding_model.embed_query(query)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
