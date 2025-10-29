# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
 
# --- 1. Definir el "Molde" de los Datos (Schema) ---
# Usamos Pydantic para decirle a FastAPI qué tipo de JSON esperamos
# para la conversión de texto.
class ItemTexto(BaseModel):
    texto: str
 
# --- 2. Crear la Aplicación FastAPI ---
app = FastAPI(
    title="API de Ejemplo",
    description="Una API simple con operaciones matemáticas y de texto."
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://dockprueba-1.onrender.com",
    "https://dockfrontend.netlify.app",
    "https://dockfronted.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# --- 3. Endpoint de Bienvenida (GET) ---
@app.get("/")
def leer_raiz():
    """Endpoint de bienvenida."""
    return {"mensaje": "Bienvenido a la API de ejemplo"}
 
# --- 4. Endpoint de Operación Matemática (GET) ---
@app.get("/sumar")
def sumar_numeros(a: int, b: int):
    """
    Suma dos números pasados como query parameters.
    Ejemplo de llamada: http://127.0.0.1:8000/sumar?a=5&b=10
    """
    resultado = a + b
    return {"numero_a": a, "numero_b": b, "suma": resultado}
 
# --- 5. Endpoint de Conversión de Texto (POST) ---
@app.post("/mayusculas")
def convertir_a_mayusculas(item: ItemTexto):
    """
    Recibe un JSON con un campo 'texto' y lo devuelve en mayúsculas.
    """
    texto_convertido = item.texto.upper()
    return {"texto_original": item.texto, "texto_convertido": texto_convertido}