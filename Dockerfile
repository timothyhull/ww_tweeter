# VS Code Python Development Container
FROM python:3.10-slim-buster

# Set the working directory
# WORKDIR /ww-tweeter
WORKDIR /workspaces/ww-tweeter

# Update OS package list and install git
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Copy the application code abd pip requirements file
# COPY app app
COPY requirements/requirements.txt requirements/requirements.txt

# Upgrade pip and install requirements from the requirements file
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt && \
    rm -rf requirements

# Set the PYTHONPATH environment variable
# ENV PYTHONPATH=/ww-tweeter
ENV PYTHONPATH=/workspaces/ww-tweeter

# Start the bash prompt
CMD ["tail", "-f", "/dev/null"]
