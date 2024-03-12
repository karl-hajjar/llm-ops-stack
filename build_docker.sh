#!/bin/bash

# build image
imagename="llm-ops-stack"
echo "Building docker image"
docker build --tag $imagename .

# Finally run container
dockerport=5000
flaskport=5000
echo "Using port $dockerport for docker container and port $flaskport for flask app"

echo "Running container"
docker run -p $flaskport:$dockerport -d $imagename
