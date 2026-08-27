from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure DevSecOps FastAPI Application!"}

@app.get("/api/data")
def get_data():
    return {
        "id": 1,
        "name":  "12345",
        "status": "active"
    }

if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8005)