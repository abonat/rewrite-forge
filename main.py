import bootstrap_tests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_adapter import LlmAdapter

app = FastAPI()


class Query(BaseModel):
    text: str
    style: str

supported_styles = [ 
    "pirate",
    "haiku",
    "formal",
    "fan of the rock band Manowar",
    "rap fan",
    "drug dealer",
    "real estate broker"
]

@app.post("/v1/rewrite")
def answer_question(query: Query):
    if query.style and query.style not in supported_styles:
        raise HTTPException(
            status_code=400,
            detail="Supported styles are:" + ','.join(supported_styles)
        )

    response = {
        "original_text": query.text,
        "transformed_text": LlmAdapter(
            prompt=query.text,
            style=query.style if query.style else 'formal'
        ).__repr__()
    }
    return {"response": response}

@app.get("/health")
def health_check():
    return { "status": "ok" }

