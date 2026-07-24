FROM python:3.9-slim

WORKDIR /app
COPY python-random.py /app/


RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

EXPOSE 8082
CMD ["python3", "python-random.py"]
