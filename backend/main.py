from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
import re

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    model: str = "deepseek-r1:7b"
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9

def remove_repetition(text: str) -> str:
    """Remove repetitive sentences from the response."""
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split into sentences
    unique_sentences = []
    for sentence in sentences:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
    return " ".join(unique_sentences)

@app.post("/api/generate")
async def generate_response(request: ChatRequest):
    try:
        print(f"Generating response with model: {request.model}")
        print(f"Prompt: {request.prompt}")
        print(f"Options: {request.temperature}, {request.top_p}, {request.max_tokens}")
        response = ollama.generate(
            model=request.model,
            prompt=request.prompt,
            options={
                'temperature': request.temperature,
                'top_p': request.top_p,  # Add top_p to options
                'max_tokens': request.max_tokens
            }
        )
        # Post-process the response to remove repetition
        cleaned_response = remove_repetition(response['response'])
        print("Response generated successfully")  # Log success
        return {"response": cleaned_response}
    except Exception as e:
        print(f"Error generating response: {str(e)}")  # Log error
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)