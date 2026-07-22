FROM python:3.12-slim AS builder                # This stage installs dependencies.
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim AS runtime                # This stage copies only the installed Python packages and app code.
WORKDIR /app
COPY --from=builder /install /usr/local
RUN useradd --create-home --shell /usr/sbin/nologin jansiuser
COPY --chown=jansiuser:jansiuser app.py .
USER jansiuser
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
