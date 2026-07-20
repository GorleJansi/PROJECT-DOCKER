FROM almalinux:9
WORKDIR /app
COPY message.txt .
RUN dnf install curl -y 
CMD ["cat","message.txt"]