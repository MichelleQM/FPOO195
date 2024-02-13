import math
lista = int(input("Ingresa la cantidad de numero que quieres en tu lista: "))

for numeros in range (lista):
    numeros = int(input("Ingresa tus numero: "))
    

def suma():
    suma = sum(numeros)
    return suma

def mayor():
    mayor = max(numeros)
    return mayor

def menor():
    menor = min(numeros)
    return menor

def promedio():
    promedio = sum(numeros)/len(numeros)
    return promedio


def menu():
    print("1. Sumatoria de los elementos")
    print("2. Numero mayor de la lista")
    print("3. Numero menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")
    
    opcion = input("Selecciona la opcion que desear usar: ")
    
    if opcion == "1":
        print("El resultado de la suma de los numeros ingresados es: ", suma)
    elif opcion == "2":
            print("El numero mayor es: ", mayor)
    elif opcion == "3":
            print("El numero menor de tu lista es: ", menor)
    elif opcion == "4":
        print("El promedio es: ", promedio)
    elif opcion == "5":
        print("La moda de tu lista es: ", )
    elif opcion == "6":
        print("El rango de tu lista es: ",)
    else:
        print("Opcion no valida")
menu()