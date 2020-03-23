#!/bin/bash

# dir
DIR=/workspace/bin
mkdir -p ${DIR}
cd ${DIR}

# kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod 0755 kubectl
