def obtener_lista():
    cantidad = int(input("Ingresa la cantidad de números que quieres en tu lista: "))
    numeros = []
    for _ in range(cantidad):
        numero = int(input("Ingresa tu número: "))
        numeros.append(numero)
    return tuple(numeros)

def suma(numeros):
    suma = sum(numeros)
    return suma

def mayor(numeros):
    mayor = max(numeros)
    return mayor

def menor(numeros):
    menor = min(numeros)
    return menor

def promedio(numeros):
    promedio = sum(numeros)/len(numeros)
    return promedio

def moda(numeros):
    return moda

def rango(numeros):
    rango = max(numeros) - min(numeros)
    return rango

def menu():
    numeros = obtener_lista()
    
    print("1. Sumatoria de los elementos")
    print("2. Numero mayor de la lista")
    print("3. Numero menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")
    
    opcion = input("Selecciona la opción que deseas usar: ")
    
    if opcion == "1":
        print("El resultado de la suma de los números ingresados es:", suma(numeros))
    elif opcion == "2":
        print("El número mayor es:", mayor(numeros))
    elif opcion == "3":
        print("El número menor de tu lista es:", menor(numeros))
    elif opcion == "4":
        print("El promedio es:", promedio(numeros))
    elif opcion == "5":
        print("La moda de tu lista es:", moda(numeros))
    elif opcion == "6":
        print("El rango de tu lista es:", rango(numeros))
    else:
        print("Opción no válida")

menu()
