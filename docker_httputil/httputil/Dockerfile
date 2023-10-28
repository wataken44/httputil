FROM wataken44/ubuntu-latest-sshd
LABEL maintainer "wataken44"

ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt update -y \
    && apt dist-upgrade -y \
    && apt install -y git-core

RUN set -xe \
    && apt update \
    && apt install -y lsb-release curl gnupg python3 python3-distutils python3-pip

RUN set -xe \
    && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt update \
    && apt install -y google-cloud-sdk google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-datastore-emulator

RUN set -xe \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && sudo apt update \
    && sudo apt install gh -y

USER ubuntu

RUN set -xe \
    && cd /home/ubuntu/ \
    && mkdir .ssh \
    && curl -SsL https://bit.ly/wataken44_id_ecdsa_pub -o .ssh/wataken44.id_ecdsa.pub \
    && cat .ssh/*.pub > .ssh/authorized_keys \
    && chmod 700 .ssh \
    && chmod 600 .ssh/* \
    && git config --global user.email wataken44@hotmail.com \
    && git config --global user.name wataken44

RUN set -xe \
    && cd /home/ubuntu/ \
    && git clone https://github.com/wataken44/httputil
    
USER root

RUN set -xe \
    && pip install -r /home/ubuntu/httputil/httputil/requirements.txt

EXPOSE 22
CMD  service ssh start && tail -f /dev/null
