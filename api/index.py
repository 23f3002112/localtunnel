from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def home():
    return "23f3002112@ds.study.iitm.ac.in"
