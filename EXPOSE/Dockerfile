FROM ubuntu:24.04
RUN apt-get update && apt-get install -y apache2 \
    && echo "ServerName localhost" >> /etc/apache2/apache2.conf
EXPOSE 80
LABEL env=dev \
     author=jansi
CMD ["apachectl", "-D", "FOREGROUND"]
