#Ingresar un valor por teclado y determinar si es positivo, negativo o igual a cero, imprimir una leyenda en cada caso
numero = float (input("Ingrese un numero"))

if numero < 0:
   print("El numero es negativo")
elif numero > 0:
   print("El numero es positivo")
else:
    print(" El numero es igual a 0")
