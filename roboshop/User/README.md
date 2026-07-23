# User Docker Setup

User is a Node.js microservice used by RoboShop for user logins and registrations.

This Docker setup uses Node.js 20 and connects User to MongoDB and Redis through a common Docker network.

## Files

- `Dockerfile` - builds the User application image.
- `.dockerignore` - keeps unnecessary files out of the Docker build context.

## Build Image

Run this command from the `roboshop/User` directory:

```bash
docker build -t user:1 .
```

To see full build logs:

```bash
docker build --progress=plain -t user:1 .
```

## Create Docker Network

Create one common network for RoboShop containers:

```bash
docker network create roboshop
```

If the network already exists, Docker will show an error. That is okay.

## Connect Dependencies To Network

MongoDB, Redis, and User must be on the same Docker network.

If MongoDB container is already running:

```bash
docker network connect roboshop mongodb
```

If Redis container is already running:

```bash
docker network connect roboshop redis
```

If a container is already connected, Docker will show an error. That is okay.

## Run User

```bash
docker run -d \
  --name user \
  --restart unless-stopped \
  --network roboshop \
  -p 8081:8080 \
  -e MONGO=true \
  -e REDIS_URL="redis://redis:6379" \
  -e MONGO_URL="mongodb://mongodb:27017/users" \
  user:1
```

The container listens on port `8080`. The host port is mapped to `8081` so it does not conflict with Catalogue if Catalogue is already using host port `8080`.

## Check Container

```bash
docker ps
docker logs user
```

## Docker Mapping

| VM / SystemD Setup | Docker Setup |
| --- | --- |
| `dnf install nodejs` | `FROM node:20-bookworm-slim` |
| `/app` application directory | `WORKDIR /app` |
| `useradd roboshop` | `RUN useradd ... roboshop` |
| `systemd Environment=...` | `docker run -e ...` |
| `systemctl start user` | `CMD ["node", "server.js"]` |
| Redis server IP address | `redis` container name on Docker network |
| MongoDB server IP address | `mongodb` container name on Docker network |

