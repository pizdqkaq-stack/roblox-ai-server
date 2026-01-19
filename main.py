from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    message: str

@app.post("/gpt")
async def gpt(msg: Msg):
    return {
        "reply": "AI ответил бесплатно 😎: " + msg.message
    }
