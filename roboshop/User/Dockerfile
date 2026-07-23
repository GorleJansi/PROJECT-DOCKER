FROM busybox:1.36 AS builder

WORKDIR /app

ADD https://roboshop-artifacts.s3.amazonaws.com/user-v3.zip /tmp/user.zip

RUN unzip /tmp/user.zip -d /app




FROM node:20-slim AS runtime

RUN useradd --no-create-home --home-dir /app --system --shell /usr/sbin/nologin --comment "roboshop system user" roboshop

WORKDIR /app

COPY --from=builder /app/ ./            
# Copies extracted app code from builder stage into final image.

RUN npm install \
    && chown -R roboshop:roboshop /app

USER roboshop
#server.js expects these env varaibles 
ENV MONGO=true
ENV REDIS_URL="redis://redis-c:6379"
ENV MONGO_URL="mongodb://mongodb-c:27017/users"

EXPOSE 8080

CMD ["node", "server.js"]



