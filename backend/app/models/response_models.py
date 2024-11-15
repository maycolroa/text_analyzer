from pydantic import BaseModel
from typing import List, Dict

class TextAnalysisResponse(BaseModel):
    word_count: int = None
    reversed_text: str = None
    word_locations: Dict[str, List[int]] = None
    unique_word_count: int = None
