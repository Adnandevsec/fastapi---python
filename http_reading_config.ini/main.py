from fastapi import FastAPI
import uvicorn
import configparser

app = FastAPI()

@app.get("/readini")
def read_from_ini():
    file = open(r"C:\Users\HP\Desktop\config.ini")
    content = file.read()
    return(content)


@app.get("/readuser")
def read_user():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\HP\Desktop\config.ini")
    value = config["database"]["username"]
    return{"value":value}


@app.get("/readpass")
def read_pass():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\HP\Desktop\config.ini")
    value = config["database"]["password"]
    return{"value":value}



if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8000)