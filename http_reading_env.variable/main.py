from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/env")
def read_env():
    v = os.getenv("user_name")
    print(v)
    return{v}

if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8003)