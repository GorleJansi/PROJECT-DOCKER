# Catalogue Docker Setup

Catalogue is a Node.js microservice used by RoboShop to serve product details.

This Docker setup uses Node.js 20 and connects Catalogue to MongoDB through a common Docker network.

## Files

- `Dockerfile` - builds the Catalogue application image.
- `.dockerignore` - keeps unnecessary files out of the Docker build context.

## Build Image

Run this command from the `roboshop/Catalogue` directory:

```bash
docker build -t catalogue:1 .
```

## Create Docker Network

Create one common network for RoboShop containers:

```bash
docker network create roboshop
```

If the network already exists, Docker will show an error. That is okay.

## Connect MongoDB To Network

MongoDB and Catalogue must be on the same Docker network.

If MongoDB container is already running:

```bash
docker network connect roboshop mongodb
```

If MongoDB is already connected, Docker will show an error. That is okay.

## Run Catalogue

```bash
docker run -d \
  --name catalogue \
  --restart unless-stopped \
  --network roboshop \
  -p 8080:8080 \
  -e MONGO=true \
  -e MONGO_URL="mongodb://mongodb:27017/catalogue" \
  catalogue:1
```

## Check Container

```bash
docker ps
docker logs catalogue
```

## Load Master Data

The `master-data.js` file is inside the Catalogue container, not inside the MongoDB container.

Use this command to load Catalogue product data into MongoDB:

```bash
docker exec -i catalogue sh -c 'cat /app/db/master-data.js' | docker exec -i mongodb mongosh mongodb://mongodb:27017/catalogue
```

## Verify Data In MongoDB

Open MongoDB shell:

```bash
docker exec -it mongodb mongosh
```

Then run:

```javascript
show dbs
use catalogue
show collections
db.products.find()
```

## Docker Mapping

| VM / SystemD Setup | Docker Setup |
| --- | --- |
| `dnf install nodejs` | `FROM node:20-bookworm-slim` |
| `/app` application directory | `WORKDIR /app` |
| `useradd roboshop` | `RUN useradd ... roboshop` |
| `systemd Environment=...` | `docker run -e ...` |
| `systemctl start catalogue` | `CMD ["node", "server.js"]` |
| MongoDB server IP address | `mongodb` container name on Docker network |

