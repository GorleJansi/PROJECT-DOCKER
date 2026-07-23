# Shipping Docker Setup

Shipping is a Java service used by RoboShop to calculate shipping distance and price.

This Docker setup builds the application with Maven and runs only the final JAR in a Java runtime image.

## Files

- `Dockerfile` - builds the Shipping application image.
- `.dockerignore` - keeps unnecessary files out of the Docker build context.

## Build Image

Run this command from the `roboshop/shipping` directory:

```bash
docker build -t shipping:v1 .
```

To see full build logs:

```bash
docker build --progress=plain -t shipping:v1 .
```

## Create Docker Network

Create one common network for RoboShop containers:

```bash
docker network create roboshop
```

If the network already exists, Docker will show an error. That is okay.

## Connect Dependencies To Network

Shipping needs Cart and MySQL on the same Docker network.

```bash
docker network connect roboshop cart-c
docker network connect roboshop mysqldb-c
```

If a container is already connected, Docker will show an error. That is okay.

## Load MySQL Schema

The SQL files are inside the Shipping image under `/app/db`.

Load schema:

```bash
docker run --rm --entrypoint sh shipping:v1 -c 'cat /app/db/schema.sql' | docker exec -i mysqldb-c mysql -uroot -p'RoboShop@1'
```

Create app user:

```bash
docker run --rm --entrypoint sh shipping:v1 -c 'cat /app/db/app-user.sql' | docker exec -i mysqldb-c mysql -uroot -p'RoboShop@1'
```

Load master data:

```bash
docker run --rm --entrypoint sh shipping:v1 -c 'cat /app/db/master-data.sql' | docker exec -i mysqldb-c mysql -uroot -p'RoboShop@1'
```

## Run Shipping

```bash
docker run -d \
  --name shipping-c \
  --restart unless-stopped \
  --network roboshop \
  -p 8083:8080 \
  -e CART_ENDPOINT="cart-c:8080" \
  -e DB_HOST="mysqldb-c" \
  shipping:v1
```

The container listens on port `8080`. The host port is mapped to `8083` so it does not conflict with other services.

## Check Container

```bash
docker ps
docker logs shipping-c
```

## Docker Mapping

| VM / SystemD Setup | Docker Setup |
| --- | --- |
| `dnf install maven` | `FROM maven:3.9-eclipse-temurin-17` |
| `mvn clean package` | `RUN mvn clean package` |
| `mv target/shipping-1.0.jar shipping.jar` | `RUN mv ... shipping.jar` |
| `/app` application directory | `WORKDIR /app` |
| `useradd roboshop` | `RUN useradd ... roboshop` |
| `systemd Environment=...` | `docker run -e ...` |
| `systemctl start shipping` | `CMD ["java", "-jar", "shipping.jar"]` |
| Cart server IP address | `cart-c` container name on Docker network |
| MySQL server IP address | `mysqldb-c` container name on Docker network |
