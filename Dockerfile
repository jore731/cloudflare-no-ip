FROM python:3.8-slim

RUN pip install requests

WORKDIR /app
COPY src src
COPY main.py main.py

CMD ["python", "/app/main.py"]