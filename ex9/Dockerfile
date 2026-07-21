FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN useradd appuser && chown -R appuser:appuser /app

USER appuser 
#Set the user name to use when running the image in addition to any subsequent CMD, ENTRYPOINT, or RUN instructions that follow it in the Dockerfile.

CMD ["python", "app.py"]