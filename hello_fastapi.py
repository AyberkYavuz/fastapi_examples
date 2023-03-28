from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
@app.get("/")
def hello_world():
    return {"message": "Hello World"}
