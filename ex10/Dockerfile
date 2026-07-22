FROM nginx:alpine
COPY ex.html /usr/share/nginx/html/index.html 
ARG city =sklm
ENV project=nginx-static \
    author=jansi \
    place=${city}
CMD ["sh", "-c", "echo HI ${author} from ${place}"]