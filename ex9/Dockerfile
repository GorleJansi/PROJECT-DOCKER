FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN useradd appuser && chown -R appuser:appuser /app

USER appuser 
#Set the user name to use when running the image in addition to any subsequent CMD, ENTRYPOINT, or RUN instructions that follow it in the Dockerfile.

EXPOSE 5000

CMD ["python", "app.py"]
