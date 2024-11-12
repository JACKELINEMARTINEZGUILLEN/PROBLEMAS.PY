# En un curso de computación, que consta de 24 alumnos, deberán armar un

#algoritmo que informe por pantalla el apellido y nombre junto a la nota de examen de cada alumno.

num_alum = 24

# Crear una lista para almacenar la información de cada alumno
alum = []

for i in range(num_alum):
    print("Ingrese los datos del alumno {i + 1}:")
    apellido = input("Ingresar pellido: ")
    nombre = input("Ingresar nombre: ")
    nota = float(input("Nota del examen: "))
    alumnos.añad({"apellido": apellido, "nombre": nombre, "nota": nota})
    print()
print("Informacion de los alumnos")
for alum in alum:
     print ("Apellido y nombre: {alumno['apellido']} {alumno['nombre']}, Nota del examen: {alumno['nota']}")
