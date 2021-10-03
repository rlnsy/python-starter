FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y pip
RUN pip install pipenv
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pipenv install --three --dev
CMD pipenv shell
