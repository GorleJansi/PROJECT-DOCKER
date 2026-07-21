FROM alpine:3.23
ENV env=dev
CMD ["sh","-c","echo current environment is ${env}"]



# [ec2-user@ip-172-31-1-179 ex7]$ docker run --name env1  env:v1
# current environment is dev

# overide the default env at runtime:
# [ec2-user@ip-172-31-1-179 ex7]$ docker run --name env1 -e env=prod env:v1
# current environment is prod

