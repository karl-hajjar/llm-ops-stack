#!/bin/bash

host="127.0.0.1"
port=5000

curl -X GET http://$host:$port/embedding/What%20is%20the%20capital%20of%20England%3F
curl -X GET http://$host:$port/chat/What%20is%20the%20capital%20of%20England%3F
curl -X GET http://$host:$port/chat/What%20is%20the%20capital%20of%20France%3F
curl -X GET http://$host:$port/chat/What%20is%202+3%3F
