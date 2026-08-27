FROM python:3.11-alpine3.24

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

RUN apk update && apk add --no-cache libffi-dev


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000


CMD ["uvicorn",  "main:app","--host","0.0.0.0","--port","8007"]



# -- create a docker ----
# docker build -t http_get:v1 .
# docker images

#---- run the docker    
#docker run -p 8000:8000 -d  http_get:v1

#docker run http_get:v1 -p 8000:8000

# -- push 
# docker login
#docker tag <local-image> <dockerhub-username>/<repository>:<tag>
# docker tag http_get:v1 adnandevsec/http_get:v1 
# docker push adnandevsec/http_get:v1


# -- pull
#docker pull adnandevsec/http_get_info:v1
#docker run -p 8001:8000 adnandevsec/http_get_info:v1

#docker stop (container id)
#docker run -d -p 8000:8000 image name
#docker rm (container id)
#docker ps
#docker ps -a

#docker inspect <container id>
#docker inspect <image name>