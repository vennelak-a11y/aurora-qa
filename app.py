from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

async def load_messages():
    url = "https://november7-730026606190.europe-west1.run.app/messages"
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        except:
            return []

def answer_question(question: str, messages: list):
    q = question.lower()
    for item in messages:
        text = item.get("message", "")
        if not text:
            continue
        t = text.lower()
        if "london" in q and "london" in t:
            return text
        if ("car" in q or "cars" in q) and ("car" in t or "cars" in t):
            return text
        if "restaurant" in q and ("restaurant" in t or "restaurants" in t):
            return text
        for word in q.split():
            if word in t:
                return text
    return "Sorry, I couldn't find an answer to that question in the member messages."

@app.post("/ask")
async def ask_question(req: QuestionRequest):
    messages = await load_messages()
    answer = answer_question(req.question, messages)
    return {"answer": answer}
