from fastapi import FastAPI
import uvicorn
import socket
import platform

app = FastAPI()

@app.get("/info")
def get_info():
    
    return {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "os": platform.system()
    }

if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8000)