FROM python:3.9-slim-buster
FROM ollama/ollama

WORKDIR /llm-ops-stack

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "llm-ops-stack/app/run.py"]
