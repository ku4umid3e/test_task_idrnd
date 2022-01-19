FROM python:3.10

WORKDIR /home

ENV API_TOKEN=""

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirenments.txt ./

RUN apt-get update && apt-get install -y cmake

RUN pip install -r requirenments.txt
COPY *.py ./

ENTRYPOINT ["python", "server.py"]
