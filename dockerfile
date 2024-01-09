FROM python:3.9

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

CMD ["python", "app.py"]
