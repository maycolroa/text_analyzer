from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import text_analyzer

app = FastAPI()

# Configura CORS para permitir el acceso desde el frontend
origins = [
    "http://localhost:8080",  # Agrega la URL del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text_analyzer.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Analyzer API"}
