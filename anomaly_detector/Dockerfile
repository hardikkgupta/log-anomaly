FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir azure-eventhub numpy
CMD ["python", "consumer.py"] 