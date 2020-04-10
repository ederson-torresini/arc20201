FROM gitpod/workspace-full

USER gitpod

RUN sudo apt-get update && \
  sudo apt-get -y install dnsutils bind9 && \
  sudo apt-get clean && \
  sudo apt-get autoremove
