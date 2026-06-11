FROM python:3.12-alpine  
#Start from an existing Docker image that contains:
#- Linux (Alpine)
#- Python 3.12

WORKDIR /app    
# Creates /app directory and makes it the current working directory  ... cd /app for example

COPY requirements.txt .
#copy requirements file from my device to the container

RUN pip install --no-cache-dir -r requirements.txt
# here will read the libraries from requirements.txt file then install them.

COPY . .
# here will copy all the project files to inside the container... for example ...(scan.py + results.json + requirements.txt)

CMD ["python", "scan.py"]
#when we run (docker run image_name) , it will execute (python scan.py)


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