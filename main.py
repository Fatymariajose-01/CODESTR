import os
import sys
from agente import interactuar_con_codestr

# Códigos de color nativos para la terminal
COLOR_BOT = '\033[96m'      # Cian
COLOR_USER = '\033[92m'     # Verde
COLOR_ERROR = '\033[91m'    # Rojo
COLOR_SISTEMA = '\033[93m'  # Amarillo
COLOR_RESET = '\033[0m'     # Restablecer color

def iniciar_chat():
    print(COLOR_SISTEMA + "=" * 60)
    print("🤖 Bienvenido a Codestr - Agente de Arquitectura de Software")
    print("Escribe 'salir' para terminar la conversación.")
    print("=" * 60 + COLOR_RESET)

    if not os.getenv("GEMINI_API_KEY"):
        print(COLOR_ERROR + "❌ Error: Clave de API inexistente. Verifica tu archivo .env." + COLOR_RESET)
        sys.exit(1)

    while True:
        try:
            print(COLOR_USER + "\n👤 Tú (Fátima): (Escribe o pega tu mensaje. Escribe 'ENVIAR' en una nueva línea para mandar)" + COLOR_RESET)
            lineas = []
            while True:
                linea = input()
                if linea.strip().upper() == 'ENVIAR':
                    break
                lineas.append(linea)
            
            mensaje = "\n".join(lineas)
            
            if mensaje.lower().strip() in ['salir', 'exit', 'quit']:
                print(COLOR_SISTEMA + "👋 ¡Éxitos en tu parcial! Nos vemos." + COLOR_RESET)
                break
            
            if not mensaje.strip():
                continue

            print(COLOR_SISTEMA + "🤖 Codestr está analizando..." + COLOR_RESET)
            
            respuesta = interactuar_con_codestr(mensaje)
            
            if not respuesta:
                print(COLOR_ERROR + "❌ Error: Se recibió una respuesta vacía del modelo." + COLOR_RESET)
                continue

            print(f"\n{COLOR_BOT}🤖 Codestr: \n{respuesta}{COLOR_RESET}")

        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "429" in error_str:
                print(COLOR_ERROR + "❌ Error: Cuota agotada de Gemini API. Usa tu nueva API Key." + COLOR_RESET)
            elif "connection" in error_str or "network" in error_str:
                print(COLOR_ERROR + "❌ Error de conexión: Revisa tu internet." + COLOR_RESET)
            elif "tool" in error_str or "function" in error_str:
                print(COLOR_ERROR + f"❌ Error en herramienta: {e}" + COLOR_RESET)
            else:
                print(COLOR_ERROR + f"❌ Ocurrió un error inesperado: {e}" + COLOR_RESET)

if __name__ == "__main__":
    iniciar_chat()