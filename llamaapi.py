from fastapi import FastAPI
from llama_cpp import Llama
from pydantic import BaseModel
import copy

app = FastAPI()

class Query(BaseModel):
    text: str

# import the model
print('loading model...')
llm = Llama(model_path="path/to/model/llamamodel.bin")
print('model loaded')

@app.post("/model")
async def analyze_email(query: Query):
    stream = llm(
        query.text,
        max_tokens=100,
        stop=["\n", " Q:"],
        echo=True,
    )

    result = stream["choices"][0]["text"].replace(query.text, "").strip()
    return {"result": result}
