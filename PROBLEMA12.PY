#Ingresar valores por teclado y acumularlos en una variable detener el proceso
#cuando la suma supere los 78500, al final imprimir el resultado

num_acumulado = 0
while num_acumulado <= 78500
     valor = float(input('Ingresar valor"))
     num_acumulado += valor
print("La suma acumulada es: {num_acumulado}")
