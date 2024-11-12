#Ingresar la nota del examen de programación y si es mayor o igual a siete imprimir que aprobó, sino que debe recuperar.
nota = int(input("Ingresar nota"))

if nota >= 70:
   print("Aprobo")
elif nota < 70:
   print("No aprobo")
print("Debe recuperarse")
