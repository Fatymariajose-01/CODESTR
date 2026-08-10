# herramientas.py

def analizar_requisitos(texto_caso: str) -> dict:
    """
    Recibe un caso y devuelve una estructura para analizar requisitos.
    """
    if not texto_caso or len(texto_caso.strip()) == 0:
        return {"error": "Caso vacío. Por favor proporciona la descripción del problema."}
    
    # En una herramienta local real, aquí podríamos usar expresiones regulares o 
    # lógica para extraer palabras clave. Por ahora, estructuramos la respuesta.
    return {
        "estado": "analizado",
        "mensaje": "Se recibió el caso correctamente. Listo para desglosar requisitos, actores, datos, restricciones y ambigüedades.",
        "longitud_texto": len(texto_caso)
    }

def revisar_codigo(codigo: str) -> dict:
    """
    Recibe un fragmento de código y devuelve una estructura para hallazgos.
    """
    if not codigo or len(codigo.strip()) == 0:
        return {"error": "Código incompleto o vacío. Proporciona el fragmento a revisar."}
    
    return {
        "estado": "revision_iniciada",
        "mensaje": "Código recibido. Listo para evaluar legibilidad, nombres, funciones extensas, duplicación, responsabilidades y manejo de errores.",
        "lineas_codigo": len(codigo.split('\n'))
    }

def generar_pruebas(funcionalidad: str) -> dict:
    """
    Recibe una funcionalidad y devuelve una estructura para casos de prueba.
    """
    if not funcionalidad or len(funcionalidad.strip()) == 0:
        return {"error": "Requisito ambiguo o vacío. Describe la funcionalidad a probar."}
    
    return {
        "estado": "pruebas_planificadas",
        "mensaje": "Funcionalidad recibida. Listo para generar caso correcto, caso incorrecto, caso límite y resultado esperado.",
        "funcionalidad_objetivo": funcionalidad
    }