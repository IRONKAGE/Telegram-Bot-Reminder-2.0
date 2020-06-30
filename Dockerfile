FROM python:3

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY . .
RUN pip3 install requests datetime

CMD [ "python", "./bot_run.py" ]
