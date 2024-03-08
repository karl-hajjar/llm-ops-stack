import os
import click
from flask import Flask, request
from datetime import datetime

from app.language_model_api import LanguageModelAPI
from utils.tools import set_up_logger, strp_datetime

FILE_DIR = os.path.dirname(__file__)

app = Flask(__name__)


@click.command()
@click.option('--host', '-h', required=False, type=click.STRING, default=None,
              help='Host address to define server')
@click.option('--port', '-p', required=False, type=click.INT, default=None,
              help='Port to communicate with the server')
@click.option('--llm_model_name', '-n', required=False, type=click.STRING, default="llama2",
              help='Which LLM model to use')
def run(host=None, port=None, llm_model_name="llama2"):
    run_dirname = strp_datetime(datetime.now())
    run_dir = os.path.join(FILE_DIR, run_dirname)
    log_path = os.path.join(run_dir, "log.txt")
    logger = set_up_logger(path=log_path)

    logger.info(f"Running LanguageModelAPI with host {host} on port {port}")
    lm_api = LanguageModelAPI(llm_model_name=llm_model_name)
    app.run(host=host, port=port)

    @app.route('/', methods=['GET'])
    def handle_prompt():
        query = request.args.get('query', type=str)
        action = request.args.get('action', default="chat", type=str)

        if action == "chat":
            result = lm_api.llm(input=query)
            return result
        elif action == "embedding":
            vector = lm_api.embedding_model(input=query)
            return vector
        else:
            raise ValueError("`action` argument must be one of 'chat' or 'embedding'")


if __name__ == "__main__":
    run()
