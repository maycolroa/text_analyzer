from typing import Dict, List

def analyze_text(text: str) -> Dict:
    # Contar palabras
    words = text.split()
    word_count = len(words)
    
    # Ubicación de cada palabra (índices en el texto)
    word_locations = {}
    for index, word in enumerate(words):
        if word not in word_locations:
            word_locations[word] = []
        word_locations[word].append(index)

    # Conteo de palabras únicas
    unique_word_count = len(set(words))

    # Texto al revés
    reversed_text = text[::-1]

    return {
        "word_count": word_count,
        "reversed_text": reversed_text,
        "word_locations": word_locations,
        "unique_word_count": unique_word_count,
    }
