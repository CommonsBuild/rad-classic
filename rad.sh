#!/bin/bash
docker build -t rad -f ./Dockerfile .
#docker run -it rad /bin/bash
docker run -it rad round-1