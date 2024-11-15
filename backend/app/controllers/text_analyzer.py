from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class TextAnalysisRequest(BaseModel):
    text: str
    operation: str
    word: str = None  # Palabra opcional para buscar

@router.post("/analyze")
def analyze_text(request: TextAnalysisRequest):
    text = request.text
    operation = request.operation
    result = {}

    if operation == 'word_count':
        result['word_count'] = len(text.split())
    elif operation == 'reverse_text':
        result['reversed_text'] = text[::-1]
    elif operation == 'character_count':
        result['character_count'] = len(text)
    elif operation == 'unique_word_count':
        result['unique_word_count'] = len(set(text.split()))
    elif operation == 'find_word':
        if not request.word:
            raise HTTPException(status_code=400, detail="No word provided for search operation")
        word_locations = [i for i, word in enumerate(text.split()) if word == request.word]
        result['word_locations'] = {request.word: word_locations}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return result
