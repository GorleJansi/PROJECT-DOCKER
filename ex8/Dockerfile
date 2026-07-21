FROM alpine:3.20

ARG APP_VERSION=1.0
   # arg takes value at image build which wont exist in container ;Define a variable with an optional default value that users can override at build-time with `docker build`.
RUN echo "Building application version ${APP_VERSION}" > /tmp/version.txt    
   # run command execute at the time of image creation

CMD ["cat", "/tmp/version.txt"]             
   # default executable which execute  at container start time 

#    docker build -t arg-demo .  --> default arg 
#    docker build --build-arg APP_VERSION=2.5   -t arg-demo .    --> buildtime give deafult args 