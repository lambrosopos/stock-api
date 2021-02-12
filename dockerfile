FROM ubuntu:latest

ENV TZ=Europe/Kiev

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y; apt-get install -y

RUN apt-get install curl wget python3-pip -y;

RUN apt-get install firefox -y

RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz -O;

RUN tar -xvzf geckodriver-v0.29.0-linux64.tar.gz -C /usr/bin;

WORKDIR /usr/src/app

COPY . .

ENV FLASK_APP=app

RUN pip3 install pipenv

RUN pipenv install --system

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]
