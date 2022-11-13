FROM python:latest

RUN pip install requests

WORKDIR /usr/app/src

COPY authentication.py ./

CMD [ "python", "./authentication.py"]