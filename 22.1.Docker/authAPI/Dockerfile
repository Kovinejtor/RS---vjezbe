FROM python:3.10-slim

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["python", "main.py"]
