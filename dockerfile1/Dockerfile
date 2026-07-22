FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN useradd --no-create-home --home-dir /app --shell /usr/sbin/nologin --system appuser && chown -R appuser:appuser /app/
USER appuser
EXPOSE 5000
ENTRYPOINT ["python","app.py"]