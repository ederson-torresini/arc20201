FROM gitpod/workspace-full
                    
USER gitpod

RUN sudo curl -L https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    sudo chmod 0755 /usr/local/bin/kubectl
