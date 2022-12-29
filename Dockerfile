FROM python:3.9-slim-buster

USER root

# Update linux and install git
RUN apt-get update && \
    apt-get install -y git

# Install pip and setuptools
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools

# Set workdir
WORKDIR /code

# Install python packages
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy files
COPY . /code/
