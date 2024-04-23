
#crea un programa que solicite un numero de 3 digitos,
# validar que se cumpla siempre esta condicion, con 
# el numero de 3 digitos calcula el valor de suma de 
# sus digitos ejemplo: numero = 435 resultado: 12

numero = input("Ingresa un numero de tres digitos: ")
suma= int(numero[0])+int(numero[1])+int(numero[2])
print("El resultado de la suma de ese digito es: ",suma)

#Realiza un programa que solicite 10 números y los almacene en una lista, una vez
#completada el usuario tendrá 2 opciones a elegir:
#1. Imprimir lista invertida
#2. Imprimir lista sin números repetidos

input("Comienza a ingresar tus 10 numeros")
numeros = [] 
for i in range(10):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero) 
opcion = int(input("Selecciona una de las dos opciones: \n 1. Imprimir lista invertida \n 2. Imprimir lista sin números repetidos: "))
if opcion == 1:
    numeros.reverse() 
    print("Tu lista invertida es:", numeros)
elif opcion == 2:
    numeros_sin_repetidos = [] 
    for numero in numeros:
        if numero not in numeros_sin_repetidos: 
            numeros_sin_repetidos.append(numero) 
    print("Tu lista sin números repetidos:", numeros_sin_repetidos)
else:    
    print("La opcion no es valida")
    

