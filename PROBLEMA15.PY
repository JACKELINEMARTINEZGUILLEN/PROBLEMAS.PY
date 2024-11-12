#Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado 
#es: a) Mayor a 0 y menor a 10
#b) Esta comprendido entre 10 y 100 ambos inclusive.
#c) Es mayor a 100
#d) Es negativo
#e) Es igual a 0
#Imprimir los resultado

Rango_mayor_0_menor_10 = 0
Rango_entre_10_y_100 = 0
Rango_mayor_100 = 0
Rango_negativo
Rango_igual_0 = 0

for x in range(100):
    valor = float(input(f"Ingrese el valor {i + 1}: "))

if valor > 0 and valor < 10:
        Rango_mayor_0_menor_10 += 1
    elif 10 <= valor <= 100:
        Rango_entre_10_y_100 += 1
    elif valor > 100:
        Rango_mayor_100 += 1
    elif valor < 0:
        Rango_negativo += 1
    elif valor == 0:
        Rango_igual_0 += 1

print("Resultados:")
print("Valores mayores a 0 y menores a 10: {Rango_mayor_0_menor_10}")
print("Valores entre 10 y 100 (ambos inclusive): {Rango_entre_10_y_100}")
print("Valores mayores a 100: {Rango_mayor_100}")
print(f"Valores negativos: {Rango_negativo}")
print(f"Valores iguales a 0: {Rango_igual_0}")
