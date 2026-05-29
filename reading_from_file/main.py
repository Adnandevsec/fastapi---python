from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/read")
def read_from_file():
    file = open(r"C:\Users\HP\Desktop\python projects\temp.txt", "r")
    content = file.read()
    file.close()
    return(content)


if __name__=="__main__":
    print("welcome..")
    uvicorn.run(app,host="127.0.0.1", port=8000)