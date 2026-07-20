# PROJECT-DOCKER

Docker practice repository for learning common Dockerfile instructions and image workflows.

## Current Examples

- `FROM/Dockerfile` - base image example using AlmaLinux.
- `RUN/Dockerfile` - installs nginx during image build.
- `CMD/Dockerfile` - starts nginx in the foreground.
- `EXPOSE/Dockerfile` - reserved for port documentation practice.
- `LABEL/Dockerfile` - reserved for image metadata practice.

## Build Order

Build the images in this order because later Dockerfiles depend on earlier local image tags.

```bash
cd FROM
docker build -t from:v1 .

cd ../RUN
docker build -t run:v1 .

cd ../CMD
docker build -t cmd:v1 .
```

## Docker Hub Push

Tag the local image with your Docker Hub username before pushing.

```bash
docker tag run:v1 jansigorle03/run:v1
docker push jansigorle03/run:v1
```

## Fix: Push Access Denied

If push fails with this error:

```text
denied: requested access to the resource is denied
```

It usually means the EC2 machine is not logged in to Docker Hub as the correct user, or the repository does not exist in Docker Hub.

Login again:

```bash
docker logout
docker login -u jansigorle03
```

If Docker Hub 2FA is enabled, use a Docker Hub personal access token instead of the account password.

Then push again:

```bash
docker push jansigorle03/run:v1
```

If it still fails, create the repository first in Docker Hub:

```text
Repository name: run
Namespace: jansigorle03
Visibility: Public or Private
```

Then retry:

```bash
docker push jansigorle03/run:v1
```
