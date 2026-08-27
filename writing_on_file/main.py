from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

class Message(BaseModel):
    name : str

@app.post("/write")
def write_on_file(mes : Message):
    file = open(r"file.txt", "a")
    file.write(mes.name+"\n")
    file.close()
    return{"message": "Written successfully"}


if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8000)