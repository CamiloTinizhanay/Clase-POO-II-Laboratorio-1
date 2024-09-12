from .estudiante import devolver_materias

# Función para determinar si un estudiante está inscrito en una materia
def estudiante_registrado_en_materia(nombre: str, materia: str) -> bool:
    try:
        materias = devolver_materias(nombre)
        return materia in materias
    except Exception as e:
        print(e)
        return False
