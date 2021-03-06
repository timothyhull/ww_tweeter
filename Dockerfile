# VS Code Python Development Container
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /workspaces/ww-tweeter

# Update OS package list and install git
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Copy the application code and pip requirements file
# COPY app app
COPY requirements/requirements.txt requirements/requirements.txt

# Upgrade pip and install requirements from the requirements file
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt && \
    rm -rf requirements

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/workspaces/ww-tweeter

# Expost TCP port 8081 to forward to bottle app on TCP port 8080
EXPOSE 8081/tcp

# Start the bash prompt
CMD ["tail", "-f", "/dev/null"]
