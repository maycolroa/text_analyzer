#Este archivo es el punto de entrada de la aplicación de FastAPI.
#Configura la API y establece los parámetros de CORS (Cross-Origin Resource Sharing)
#para permitir que el frontend acceda a la API.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import text_analyzer

#crea una intancia de la clase fastapi es la aplicacion principal 
app = FastAPI()

# Configura CORS para permitir el acceso desde el frontend
origins = [
    "http://localhost:8080",  # Agrega la URL del frontend
]

# allow_origins=origins: Permite solicitudes solo desde las URL definidas en origins 
# (en este caso, http://localhost:8080).
# allow_credentials=True: Permite que se envíen cookies y credenciales con las solicitudes.
# allow_methods=["*"]: Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.) en las solicitudes.
#allow_headers=["*"]: Permite todos los encabezados en las solicitudes

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incorporación de Rutas desde el Controlador: 
# Aquí se usa include_router para agregar las rutas definidas en el módulo text_analyzer 
# a la aplicación app. text_analyzer.router se refiere a un objeto APIRouter que organiza 
# esto permite una estructura modular en el proyecto, 
# separando las rutas en diferentes archivos o módulos.

app.include_router(text_analyzer.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Analyzer API"}
