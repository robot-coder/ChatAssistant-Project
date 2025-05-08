from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Define a model for the user input
class UserInput(BaseModel):
    prompt: str
    llm_choice: str

# Store conversation history
conversation_history = []

@app.post("/chat/")
async def chat(input: UserInput):
    # Append user message to conversation history
    conversation_history.append({'role': 'user', 'content': input.prompt})

    # Here you would call the LiteLLM API based on the user's choice
    response = requests.post(f"https://api.litelm.com/{input.llm_choice}", json={"prompt": input.prompt})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error calling LLM")
    assistant_response = response.json().get('response')

    # Append assistant response to conversation history
    conversation_history.append({'role': 'assistant', 'content': assistant_response})

    return {'response': assistant_response, 'history': conversation_history}