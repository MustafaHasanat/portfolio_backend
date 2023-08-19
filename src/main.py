from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/", status_code=201)
def hello():
    return {"Hello": "World"}