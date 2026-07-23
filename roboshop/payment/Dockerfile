
FROM busybox:1.36 AS source
WORKDIR /app
ADD  https://roboshop-artifacts.s3.amazonaws.com/payment-v3.zip  /tmp/payment.zip
RUN unzip /tmp/payment.zip

FROM python:3.12-slim AS builder
WORKDIR /app
COPY --from=source /app/ ./
RUN pip3 install -r requirements.txt
USER roboshop

FROM python:3.12-slim AS runtime
WORKDIR /app
COPY --from=builder /app/payment.ini ./
RUN useradd --system --home-dir /app --shell /sbin/nologin --comment "roboshop system user" roboshop
ENV CART_HOST=cart-c
ENV CART_PORT=8080
ENV USER_HOST=user-c
ENV USER_PORT=8080
ENV AMQP_HOST=rabbitmq-c
ENV AMQP_USER=roboshop
ENV AMQP_PASS=roboshop123

CMD ["usr/local/bin/uwsgi" "--ini" "payment.ini"]