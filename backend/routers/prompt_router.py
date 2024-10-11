
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.prompt_generator import PromptGenerator

router = APIRouter(prefix="/prompt", tags=["Prompt Generation"])

prompt_gen = PromptGenerator()

class PromptRequest(BaseModel):
    input_text: str
    max_length: int = 50

@router.post("/generate_prompt")
async def generate_prompt(request: PromptRequest):
    try:
        prompt = prompt_gen.generate_prompt(request.input_text, request.max_length)
        return {"prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
