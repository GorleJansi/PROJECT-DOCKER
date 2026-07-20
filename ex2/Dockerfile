FROM almalinux:9
WORKDIR /app
RUN pwd
COPY message.txt .
RUN dnf install curl -y --allowerasing
CMD ["cat","message.txt"]