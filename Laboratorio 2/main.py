from instituto.clase import estudiante_registrado_en_materia

# Pruebas con la función estudiante_registrado_en_materia
print(estudiante_registrado_en_materia("Daniel", "Matematica"))  # True
print(estudiante_registrado_en_materia("Daniel", "Biologia"))    # False
print(estudiante_registrado_en_materia("Maria", "Fisica"))       # True
print(estudiante_registrado_en_materia("Juan", "Matematica"))    # El estudiante Juan no está registrado.
