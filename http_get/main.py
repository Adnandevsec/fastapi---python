from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    
    return {"Hello"}

if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8000)
