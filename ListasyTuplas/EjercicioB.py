import random

def numeros_lista():
    lista = [random.randint(10, 20) for _ in range(30)]
    return lista

def contar_repetidos(lista):
    repeticiones = {}
    for num in lista:
        if num in repeticiones:
            repeticiones[num] += 1
        else:
            repeticiones[num] = 1
    return repeticiones

def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

def reemplazar_con_ceros(lista):
    return lista

def main():
    lista = numeros_lista()
    print("Lista generada:", lista)
    
    print("1. Contar los numeros repetidos de tu lista")
    print("2. Elimina el numero que mas se repite")
    print("3. Remplaza el numero mas repetido con 0")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        repeticiones = contar_repetidos(lista)
        print("Número de repeticiones de cada valor:", repeticiones)
    elif opcion == "2":
        lista_sin_repetidos = eliminar_repetidos(lista)
        print("Lista sin valores repetidos:", lista_sin_repetidos)
    elif opcion == "3":
        lista_reemplazada = reemplazar_con_ceros(lista)
        print("Lista con valores repetidos reemplazados por 0:", lista_reemplazada)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


