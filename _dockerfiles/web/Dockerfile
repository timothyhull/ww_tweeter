# Dockerfile for bottle web application
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /web

# Expose the web service port
EXPOSE 8080/tcp

# Update OS packages
RUN apt-get update && \
    apt-get upgrade -y

# Copy the pip requirements file
COPY requirements/requirements.txt requirements/requirements.txt

# Upgrade pip and install requirements from the requirements file
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt && \
    rm -rf requirements

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/web

# Start the bottle server
# CMD ["python", "_dockerfiles/web/__dev__/bottle_testing.py"]
CMD ["tail", "-f", "/dev/null"]
