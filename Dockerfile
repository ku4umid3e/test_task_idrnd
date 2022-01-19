FROM python:3.10

WORKDIR /home

ENV API_TOKEN=""

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt
COPY *.py ./

ENTRYPOINT ["python", "server.py"]
