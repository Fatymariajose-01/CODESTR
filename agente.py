# 1. Importa os y utilidades
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 4. Importa las instrucciones
from instrucciones import Instrucciones_agente

# 5. Importa las herramientas
from herramientas import analizar_requisitos, revisar_codigo, generar_pruebas

# 2. Carga las variables de entorno (lee el archivo .env oculto)
load_dotenv()

# 3. Crea el cliente del SDK (automáticamente usa la GEMINI_API_KEY)
client = genai.Client()

# Configuración central del agente
config = types.GenerateContentConfig(
    system_instruction=Instrucciones_agente, # <--- Dónde se envían las instrucciones
    tools=[analizar_requisitos, revisar_codigo, generar_pruebas], # <--- Dónde se registran las herramientas
    temperature=0.2, # Temperatura baja para respuestas más técnicas y precisas
)

# Creamos una sesión de chat para que Codestr tenga "memoria" de la conversación
chat = client.chats.create(
    model="models/gemini-3.5-flash", 
    config=config
)

# 6. Configura una función que reciba el mensaje del usuario
def interactuar_con_codestr(mensaje_usuario: str) -> str:
    """
    Toma el mensaje, lo envía a Gemini y devuelve la respuesta.
    Gemini decidirá aquí si necesita ejecutar una herramienta.
    """
    # Dónde se detecta la llamada y se ejecuta la función
    respuesta = chat.send_message(mensaje_usuario)
    
    # Dónde se devuelve el resultado
    return respuesta.text