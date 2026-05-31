FROM python:3-slim

EXPOSE 8000

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["uvicorn",  "main:app","--host","0.0.0.0","--port","8000"]

# -- create a docker ----
# docker build -t http_get:v1 .
# docker images

#---- run the docker 
#docker run -p 8000:8000 -d  http_get:v1
 
#docker run http_get:v1 -p 8000:8000

#--- Push image 
# docker login
# docker push ...............
