from dotenv import load_dotenv
from google import genai

# Cargar la clave de API
load_dotenv()

# Crear el cliente
client = genai.Client()

print("🔍 Buscando modelos disponibles para tu API Key...")
print("-" * 40)

# Listar e imprimir el nombre de cada modelo
try:
    for modelo in client.models.list():
        # Filtramos un poco para ver solo los de la familia gemini
        if "gemini" in modelo.name:
            print(modelo.name)
except Exception as e:
    print(f"❌ Error al conectar con la API: {e}")

print("-" * 40)