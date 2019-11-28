FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev



WORKDIR /app

RUN pip install flask && \
        pip install requests &&\
		pip install pymysql

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "lambda_function.py" ]
