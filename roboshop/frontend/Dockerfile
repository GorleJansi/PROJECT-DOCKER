FROM busybox:1.36 AS source

WORKDIR /usr/share/nginx/html

ADD https://roboshop-artifacts.s3.amazonaws.com/frontend-v3.zip /tmp/frontend.zip

RUN unzip /tmp/frontend.zip -d /usr/share/nginx/html


FROM nginx:1.24

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=source /usr/share/nginx/html/ /usr/share/nginx/html/

EXPOSE 80
