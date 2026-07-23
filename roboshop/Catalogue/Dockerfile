FROM busybox:1.36 AS builder

WORKDIR /app

ADD https://roboshop-artifacts.s3.amazonaws.com/catalogue-v3.zip /tmp/catalogue.zip

RUN unzip /tmp/catalogue.zip -d /app


FROM node:20-bookworm-slim AS runtime

RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin --comment "roboshop system user" roboshop

WORKDIR /app

COPY --from=builder /app/ ./

RUN npm install \
    && chown -R roboshop:roboshop /app

USER roboshop

ENV MONGO=true
ENV MONGO_URL="mongodb://mongodb-c:27017/catalogue"
ENV REDIS_URL="redis://redis-c:6379"
EXPOSE 8080

CMD ["node", "server.js"]



# VM:
# systemctl start user
#         ↓
# systemd reads /etc/systemd/system/user.service
#         ↓
# ExecStart=/bin/node /app/server.js
#         ↓
# Node.js starts custom code

# Docker:
# docker run catalogue:v1
#         ↓
# Docker reads image CMD
#         ↓
# CMD ["node", "server.js"]
#         ↓
# Node.js starts custom code