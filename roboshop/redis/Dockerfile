FROM redis:7
COPY redis.conf /usr/local/etc/redis/redis.conf
EXPOSE 6379
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]


# [ec2-user@ip-172-31-1-179 redis]$ docker exec -it redis-cache redis-cli ping
# PONG