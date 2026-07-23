# Frontend Docker Setup

Frontend serves RoboShop static web content through Nginx and proxies API calls to backend containers.

## Files

- `Dockerfile` - builds the Nginx frontend image.
- `nginx.conf` - reverse proxy configuration for backend services.
- `.dockerignore` - keeps unnecessary files out of the Docker build context.

## Build Image

Run this command from the `roboshop/frontend` directory:

```bash
docker build -t frontend:v1 .
```

To see full build logs:

```bash
docker build --progress=plain -t frontend:v1 .
```

## Create Docker Network

Create one common network for RoboShop containers:

```bash
docker network create roboshop
```

If the network already exists, Docker will show an error. That is okay.

## Run Frontend

```bash
docker run -d \
  --name frontend-c \
  --restart unless-stopped \
  --network roboshop \
  -p 80:80 \
  frontend:v1
```

## Backend Names Used By Nginx

The reverse proxy uses Docker container names and container ports:

| API path | Backend target |
| --- | --- |
| `/api/catalogue/` | `catalogue-c:8080` |
| `/api/user/` | `user-c:8080` |
| `/api/cart/` | `cart-c:8080` |
| `/api/shipping/` | `shipping-c:8080` |
| `/api/payment/` | `payment-c:8080` |

All backend containers must be connected to the `roboshop` Docker network.

## Check

```bash
docker ps
docker logs frontend-c
curl http://localhost/health
```

Browser:

```text
http://<EC2-PUBLIC-IP>/
```
