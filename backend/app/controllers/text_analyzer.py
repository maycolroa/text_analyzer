from fastapi import APIRouter, HTTPException 
from pydantic import BaseModel 

# Creación del enrutador
router = APIRouter()  # Creamos una instancia de APIRouter para definir las rutas en este archivo

# Modelo de solicitud
class TextAnalysisRequest(BaseModel):
    # Definimos el modelo de datos que esperamos recibir en la solicitud
    text: str  # El texto a analizar
    operation: str  # El tipo de operación a realizar en el texto
    word: str = None  # Palabra opcional para operaciones de búsqueda específicas
    toReplace: str = None  # Palabra que queremos reemplazar en el texto (opcional)
    replacement: str = None  # Nueva palabra con la que reemplazar la palabra anterior (opcional)
    list_to_join: list = None  # Lista opcional de palabras que se unirán en una sola cadena

# Definición de la ruta para el análisis de texto
@router.post("/analyze")
def analyze_text(request: TextAnalysisRequest):
    # Extraemos los datos de la solicitud
    text = request.text  # Texto sobre el cual se realizará la operación
    operation = request.operation  # Tipo de operación que el usuario solicitó
    result = {}  # Diccionario donde se almacenará el resultado de la operación

    # Operaciones de análisis de texto según el valor de `operation`
    if operation == 'word_count':
        # Cuenta el número de palabras en el texto
        result['word_count'] = len(text.split())  # Divide el texto en palabras y cuenta la longitud de la lista

    elif operation == 'reverse_text':
        # Invierte el texto
        result['reversed_text'] = text[::-1]  # Usa slicing para invertir el texto

    elif operation == 'character_count':
        # Cuenta el número de caracteres en el texto
        result['character_count'] = len(text)  # Usa len() para contar los caracteres en la cadena

    elif operation == 'unique_word_count':
        # Cuenta el número de palabras únicas en el texto
        result['unique_word_count'] = len(set(text.split()))  # Usa un set para eliminar duplicados y cuenta su longitud

    elif operation == 'find_word':
        # Encuentra todas las posiciones de una palabra específica en el texto
        if not request.word:  # Verifica si se proporcionó una palabra
            raise HTTPException(status_code=400, detail="No word provided for search operation")
        # Encuentra la posición de cada aparición de la palabra en el texto
        word_locations = [i for i, word in enumerate(text.split()) if word == request.word]
        result['word_locations'] = {request.word: word_locations}  # Guarda las posiciones en el resultado

    elif operation == 'uppercase':
        # Convierte el texto a mayúsculas
        result['uppercase_text'] = text.upper()  # Convierte el texto en mayúsculas

    elif operation == 'join_list':
        # Une los elementos de una lista en una sola cadena, separados por espacios
        if not request.list_to_join:  # Verifica si se proporcionó una lista para unir
            raise HTTPException(status_code=400, detail="No list provided to join")
        result['joined_text'] = " ".join(request.list_to_join)  # Une los elementos de la lista en una cadena

    elif operation == 'replace_words':
        # Reemplaza una palabra específica en el texto por otra palabra
        if not request.toReplace or not request.replacement:  # Verifica si se proporcionaron las palabras
            raise HTTPException(status_code=400, detail="Both 'toReplace' and 'replacement' must be provided")
        # Reemplaza todas las ocurrencias de `toReplace` con `replacement`
        result['replaced_text'] = text.replace(request.toReplace, request.replacement)

    else:
        # Si el valor de `operation` no coincide con ninguna operación definida, se lanza un error
        raise HTTPException(status_code=400, detail="Invalid operation")

    # Retorna el resultado en formato JSON
    return result
