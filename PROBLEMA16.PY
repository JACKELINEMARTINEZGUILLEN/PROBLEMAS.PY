#Ingresar 10 valores numéricos y obtener el promedio de los que estén comprendidos entre 5 y 2500 ambos inclusive, imprimir el resultado
suma = 0 
numeros_validos = 0

for x in range(10):
    valor = float(input("Ingrese el valor {i + 1}: "))
    if 5 <= valor <= 2500:
       suma += valor
       numero_validos += 1
if numeros_validos > 0:
    promedio = suma / nuemro_validos
    print("El promedio de los valores entre 5 y 2500 es:", promedio)
