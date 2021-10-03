FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y "python3.9"
RUN apt-get install -y python3.9-venv
RUN apt-get install -y pip
RUN "python3.9" -m pip install tox tox-venv
RUN mkdir /app
WORKDIR /app
COPY . .
RUN tox
