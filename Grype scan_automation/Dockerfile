FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "scan.py"]



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