FROM python:3.10
ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /app/requirements.txt
# RUN pip install --upgrade pip

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
