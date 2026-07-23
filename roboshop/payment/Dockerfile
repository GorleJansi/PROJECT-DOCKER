FROM busybox:1.36 AS source
WORKDIR /app
ADD https://roboshop-artifacts.s3.amazonaws.com/payment-v3.zip /tmp/payment.zip
RUN unzip /tmp/payment.zip -d /app


FROM python:3.12 AS runtime
RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin --comment "roboshop system user" roboshop
WORKDIR /app
COPY --from=source /app/ ./
RUN pip3 install --no-cache-dir -r requirements.txt && chown -R roboshop:roboshop /app
USER roboshop
ENV CART_HOST=cart-c
ENV CART_PORT=8080
ENV USER_HOST=user-c
ENV USER_PORT=8080
ENV AMQP_HOST=rabbitmq-c
ENV AMQP_USER=roboshop
ENV AMQP_PASS=roboshop123

EXPOSE 8080

CMD ["/usr/local/bin/uwsgi", "--ini", "payment.ini"]
