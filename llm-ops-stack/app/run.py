import os
import click
from flask import Flask
from datetime import datetime
import json
from collections import OrderedDict

from app.language_model_api import LanguageModelAPI
from utils.tools import set_up_logger, strp_datetime

FILE_DIR = os.path.dirname(__file__)
app = Flask(__name__)
HOST = "0.0.0.0"


@click.command()
@click.option('--host', '-h', required=False, type=click.STRING, default="0.0.0.0",
              help='Host address to define server')
@click.option('--port', '-p', required=False, type=click.INT, default=None,
              help='Port to communicate with the server')
@click.option('--llm_model_file', '-f', required=False, type=click.STRING, default="llama-2-7b-chat.Q4_K_M.gguf",
              help='Which LLM model to use')
def run(host="0.0.0.0", port=None, llm_model_file="llama-2-7b-chat.Q4_K_M.gguf"):
    if host is None or host == "":
      host = HOST
    run_dirname = strp_datetime(datetime.now())
    run_dir = os.path.join(FILE_DIR, 'runs', run_dirname)
    os.makedirs(run_dir, exist_ok=True)

    log_path = os.path.join(run_dir, "log.txt")
    global logger
    logger = set_up_logger(path=log_path)

    global lm_api
    lm_api = LanguageModelAPI(llm_model_file=llm_model_file)

    logger.info(f"App launched, waiting for requests...")
    logger.info(f"Parameters passed to the Flask app: host={host} on port={port}")
    app.run(host=host, port=port)


@app.route('/', methods=['GET'])
def hello():
    return f"<h1>Hello, you are about to interact with the LLM {lm_api.llm_model_file} !</h1>"


@app.route('/chat/<query>', methods=['GET'])
def chat(query: str):
    result = lm_api.llm(query).strip()
    formatted_query = f"User query : {query}"
    formatted_answer = f"Assistant answer : {result}"
    logger.info(formatted_query)
    logger.info(formatted_answer)
    return_dict = OrderedDict({"User query": query.strip(),
                               "Assistant answer": result})
    return json.dumps(return_dict)


@app.route('/embedding/<query>', methods=['GET'])
def embed(query: str):
    vector = lm_api.embedding_model.encode(query)
    return_dict = OrderedDict({"query": query,
                               "embedding_size": len(vector),
                               "embedding": vector.tolist()})
    return json.dumps(return_dict)


if __name__ == "__main__":
    run()
