FROM python:3.12-slim AS builder              
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim AS runtime               
WORKDIR /app
COPY --from=builder /install /usr/local
RUN useradd --create-home --shell /usr/sbin/nologin jansiuser
COPY --chown=jansiuser:jansiuser app.py .
USER jansiuser
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]


# stage 1: install/build dependencies
# stage 2: copy only final needed output from builder stage and run app
# builder image:
# python + gcc + build tools + dependencies

# runtime image:
# python + installed app dependencies + app code

# Build the Python image:
# docker build -t python-multistage:v1 .
# Check the image:
# docker images python-multistage