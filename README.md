# LLM OPS stack
A repository for hosting an llm api with all the necessary stack.

## Setting up the repository

First clone the repository:
```bash
git clone git@github.com:karl-hajjar/llm-ops-stack.git
``` 

Then go to the root directory `llm-ops-stack`of the repo:
```bash
cd llm-ops-stack
```

Then create a virtual environment with all the necessary packages. Run the following commands one by one sequentially:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
If the latter `pip install` command fails with a CMAKE error, simply run 
```bash
pip install "huggingface-hub>=0.17.1"
```

Finally download the Llama2-7b LLM from the HuggingFace hub:
```bash 
huggingface-cli download TheBloke/Llama-2-7b-Chat-GGUF llama-2-7b-chat.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```
(see [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)).

## Running the Language Model API in a Docker container
If Docker is already installed (otherwise, see [here](https://docs.docker.com/engine/install/)), launch it and simply run
```bash
bash build_docker.sh
```

This will take a while to copy all the necessary files and install all the necessary packages inside the docker 
container. After the image is built and running, wait a little more for the API to load the LLM into memory (this can 
take some time as well) and then finally go to the URL: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the 
Language model API up and running. 

To send requests to the API you can either directly modify the link to the URL as such:
[http://127.0.0.1:5000/chat/What%20is%20the%20capital%20of%20England%3F](http://127.0.0.1:5000/chat/What%20is%20the%20capital%20of%20England%3F)
or 
[http://127.0.0.1:5000/embedding/What%20is%20the%20capital%20of%20England%3F](http://127.0.0.1:5000/embedding/What%20is%20the%20capital%20of%20England%3F).
Otherwise you can use the script `send_example_requests.sh` to see the response to different requests.






