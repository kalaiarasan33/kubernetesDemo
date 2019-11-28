FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev



WORKDIR /app

RUN pip install flask && \
        pip install requests

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "my_app.py" ]
