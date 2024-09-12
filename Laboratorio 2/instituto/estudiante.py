from typing import List, Dict

# Diccionario con estudiantes y las materias que cursan
estudiantes: Dict[str, List[str]] = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

# Función para devolver las materias que cursa un estudiante
def devolver_materias(nombre: str) -> List[str]:
    try:
        return estudiantes[nombre]
    except KeyError:
        raise Exception(f"El estudiante {nombre} no está registrado.")
