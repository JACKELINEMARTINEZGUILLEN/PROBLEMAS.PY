#Calcular la nota del trimestre a partir de tres notas, luego determinar si aprobó o debe recuperar e informarlo.

nota1 = int(input("Ingresar nota"))
nota2 = int(input("Ingresar nota"))
nota3 = int(input("Ingresar nota"))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 70:
   print("Aprobo")
elif promedio < 70:
   print("No aprobo")
print("Debe recuperarse")
