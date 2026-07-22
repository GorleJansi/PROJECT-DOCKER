FROM nginx:alpine
COPY ex.html /usr/share/nginx/html/index.html 
ARG city=sklm
ENV project=nginx-static \
    author=jansi \
    place=${city}
CMD ["sh", "-c", "echo HI ${author} from ${place}"]


# [ec2-user@ip-172-31-1-179 ex10]$ docker run --rm --name ex10-nginx-v2 -p 81:80 -e author=munni ex10:v2
# HI munni from hyd
# [ec2-user@ip-172-31-1-179 ex10]$ docker run --name ex10-nginx-v1 -p 81:80 ex10:v1
# HI jansi from sklm
# [ec2-user@ip-172-31-1-179 ex10]$ docker run --name ex10-nginx-v2 -p 81:80 ex10:v2
# HI jansi from hyd