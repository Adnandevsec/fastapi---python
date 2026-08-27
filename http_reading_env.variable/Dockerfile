FROM python:alpine:3.23

EXPOSE 8000

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV user_name=sari
LABEL developer="Adnan"


CMD ["uvicorn",  "main:app","--host","0.0.0.0","--port","8000"]



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
#docker start (container id)
#docker rm (container id)
#docker image rm (image name)
#docker ps
#docker ps -a

# ---container shell access (login to the container)
#docker exec -it <container_name_or_id> bash
#docker exec -it <container_name_or_id> sh

#--- see container logs
##docker logs (container Id)
#docker logs -f (container Id)   - to see the real-time logs 


#docker inspect <container id>
#docker inspect <image name>