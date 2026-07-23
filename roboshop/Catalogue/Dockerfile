FROM node:20-bookworm-slim AS builder

RUN apt-get update && apt-get install -y curl unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -o /tmp/catalogue.zip https://roboshop-artifacts.s3.amazonaws.com/catalogue-v3.zip \
    && unzip /tmp/catalogue.zip \
    && rm /tmp/catalogue.zip




    
FROM node:20-bookworm-slim AS runtime

RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin --comment "roboshop system user" roboshop

WORKDIR /app

COPY --from=builder /app/ ./

RUN npm install \
    && chown -R roboshop:roboshop /app

USER roboshop

ENV MONGO=true
ENV MONGO_URL="mongodb://mongodb:27017/catalogue"

EXPOSE 8080

CMD ["node", "server.js"]