FROM node:20-bookworm-slim AS builder

RUN apt-get update && apt-get install -y curl unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -L -o /tmp/user.zip https://roboshop-artifacts.s3.amazonaws.com/user-v3.zip \
    && unzip /tmp/user.zip \
    && rm /tmp/user.zip


FROM node:20-bookworm-slim AS runtime

RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin --comment "roboshop system user" roboshop

WORKDIR /app

COPY --from=builder /app/ ./

RUN npm install \
    && chown -R roboshop:roboshop /app

USER roboshop

ENV MONGO=true
ENV REDIS_URL="redis://redis:6379"
ENV MONGO_URL="mongodb://mongodb:27017/users"

EXPOSE 8080

CMD ["node", "server.js"]
