FROM busybox:1.36 AS source
WORKDIR /app
ADD https://roboshop-artifacts.s3.amazonaws.com/shipping-v3.zip /tmp/shipping.zip
RUN unzip /tmp/shipping.zip -d /app
# from source stage unzip and get files inside

FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY --from=source /app/ ./
RUN mvn clean package && mv target/shipping-1.0.jar shipping.jar
# from builder stage install dependencies and compile

FROM eclipse-temurin:17-jre AS runtime
RUN useradd --system --home-dir /app --shell /usr/sbin/nologin --comment "roboshop system user" roboshop
WORKDIR /app
COPY --from=builder /app/shipping.jar ./
COPY --from=source /app/db ./db

RUN chown -R roboshop:roboshop /app

USER roboshop

ENV CART_ENDPOINT="cart-c:8080"
ENV DB_HOST="mysqldb-c"

EXPOSE 8080

CMD ["java", "-jar", "shipping.jar"]





# 1 stage: unzip the zip file
# 2 stage: compile the file; get unziped files from 1 stage
# 3 stage: run the compiled file; get compiled file and required files from 2 stage