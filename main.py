from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Define a model for the user input
class UserInput(BaseModel):
    prompt: str
    llm_choice: str

@app.post("/chat/")
async def chat(input: UserInput):
    # Here you would call the LiteLLM API based on the user's choice
    response = requests.post(f"https://api.litelm.com/{input.llm_choice}", json={"prompt": input.prompt})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error calling LLM")
    return response.json()