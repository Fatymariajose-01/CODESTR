# 🤖 Codestr - Agente de Arquitectura de Software

Codestr es un agente de Inteligencia Artificial diseñado para asistir en procesos de ingeniería de software. A diferencia de un chatbot tradicional, Codestr está configurado para actuar como un arquitecto de software crítico: detecta ambigüedades en los requerimientos, exige especificaciones claras antes de programar y audita fragmentos de código aplicando principios de diseño limpio (SOLID, KISS, DRY).

Este proyecto fue desarrollado para la validación de requerimientos y auditoría de sistemas, permitiendo transicionar de peticiones ambiguas a especificaciones funcionales y código modular.

## ✨ Características Principales

* **Auditoría de Requerimientos:** Analiza peticiones de sistemas (ej. "sistema de ventas") y genera preguntas clave y casos límite antes de proponer una arquitectura.
* **Revisión de Código Estricta:** Implementa herramientas (tools) para analizar código, detectando malas prácticas, vulnerabilidades (como inyección SQL) y acoplamiento fuerte.
* **Interfaz de Consola Multilínea:** Sistema de entrada robusto que permite pegar bloques completos de código y especificaciones sin colapsar la terminal.
* **Manejo de Errores y Cuotas:** Gestión segura de interrupciones, límites de peticiones (RPM) de la API y manejo de variables de entorno.

## 🛠️ Tecnologías y Requisitos

* **Lenguaje:** Python 3.x
* **Integración IA:** `google-genai` SDK (Gemini API - Modelo Flash)
* **Gestión de Entorno:** `python-dotenv`

## 🚀 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Fatymariajose-01/CODESTR.git
   cd agente_codestr 

 Crear y activar un entorno virtual:

En Windows:

Bash
python -m venv .venv
.venv\Scripts\activate
En macOS/Linux:

Bash
python3 -m venv .venv
source .venv/bin/activate
Instalar dependencias:

Bash
pip install google-genai python-dotenv
Configurar las credenciales:
Crea un archivo llamado .env en la raíz del proyecto y agrega tu clave de API de Google Gemini:

Fragmento de código

GEMINI_API_KEY=tu_clave_de_api_aqui

💻 Uso del Agente
Para iniciar la interacción con Codestr, ejecuta el archivo principal desde tu terminal:

Bash

python main.py

📝 Cómo enviar mensajes (Importante)
El sistema está diseñado para soportar entradas de múltiples líneas (ideal para pegar código o especificaciones largas). Para enviar tu mensaje a la IA:

Escribe o pega tu texto.

Presiona Enter para ir a una línea nueva.

Escribe la palabra ENVIAR (en mayúsculas).

Presiona Enter nuevamente.

Para salir del programa, escribe salir y presiona Enter.

📂 Estructura del Proyecto

main.py: Punto de entrada del programa. Maneja la interfaz de consola, la captura multilínea y la gestión de errores/colores.

agente.py: Configuración del cliente google-genai, definición de las instrucciones del sistema y orquestación de la memoria conversacional.

herramientas.py: Definición de herramientas locales que la IA puede invocar, como la función de revisar_codigo.

.env: Archivo de variables de entorno (no incluido en el repositorio por seguridad).


