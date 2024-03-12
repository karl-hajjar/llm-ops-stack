# FROM ubuntu
# ENV DEBIAN_FRONTEND noninteractive
# RUN apt-get update && \
#     apt-get -y install gcc-11 mono-mcs && \
#     rm -rf /var/lib/apt/lists/*

#FROM python:3.9-slim-buster
FROM python

WORKDIR /llm-ops-stack

# RUN pip install llama-cpp-python

COPY requirements.txt requirements.txt

#RUN pip install --upgrade pip
#RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR llm-ops-stack/
ENV PYTHONPATH "${PYTHONPATH}:$PWD"

CMD [ "python3", "app/run.py"]
