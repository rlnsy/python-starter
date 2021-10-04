FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y "python3.9"
RUN apt-get install -y python3.9-venv
RUN apt-get install -y "python3.8"
RUN apt-get install -y python3.8-venv
RUN apt-get install -y pip
RUN "python3.9" -m pip install tox tox-venv
RUN mkdir /app
WORKDIR /app
COPY . .
RUN tox
# set up the environment - this replicates the venv activate behaviour.
# Thanks to this post:
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=.tox/py39
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD bash
