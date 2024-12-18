FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask==3.1.0 psycopg2-binary==2.9.7

EXPOSE 5000
CMD ["python", "app.py"]
