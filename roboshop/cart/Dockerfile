FROM busybox:1.36 AS builder
WORKDIR /app
ADD https://roboshop-artifacts.s3.amazonaws.com/cart-v3.zip /tmp/cart.zip
RUN unzip -d /tmp/cart.zip  /app



FROM node:20-slim AS runtime
RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin roboshop
WORKDIR /app
COPY --from=builder /app/ ./
RUN npm install && chown -R roboshop:roboshop /app
USER roboshop
ENV REDIS_HOST=redis-c
ENV CATALOGUE_HOST=catalogue-c
ENV CATALOGUE_PORT=8080
CMD ["node","server.js"]