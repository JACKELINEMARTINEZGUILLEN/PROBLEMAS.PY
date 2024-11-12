#Ingresar un valor por teclado y determinar si es menor que 10 si está comprendido
#entre 10 y 100 o si es mayor a 100, imprimir una leyenda, repetir el proceso 10 veces

for x in range (10):
     valor = float(input("Ingresar el valor {x + 1}:"))

     if valor < 10:
        print("El valor es menor que 10")
     elif valor >= 100:
        print("El valor esta entre 10 y 100")
     else:
        print("El valor es mayor a 100")
