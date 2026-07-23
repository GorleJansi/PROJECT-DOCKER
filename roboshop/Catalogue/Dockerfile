FROM node:20-bookworm-slim AS builder

WORKDIR /app

ADD https://roboshop-artifacts.s3.amazonaws.com/catalogue-v3.zip /tmp/catalogue.zip

RUN npm install -g adm-zip \
    && node -e "require('adm-zip')('/tmp/catalogue.zip').extractAllTo('/app', true)" \
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