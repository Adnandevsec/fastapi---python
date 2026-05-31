FROM python:3-slim

EXPOSE 8000

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["uvicorn",  "main:app","--host","0.0.0.0","--port","8000"]
