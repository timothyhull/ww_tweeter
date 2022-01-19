# VS Code Python Development Container
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /workspaces/ww-tweeter

RUN apt-get update && \
    apt-get install -y git

COPY requirements/requirements.txt requirements/requirements.txt

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt

ENV PYTHONPATH=/workspaces/ww-tweeter

CMD ["/bin/bash"]
