numero = int(input("ingrese un numero para la base del arbol: "))
i = numero - 1
j = 1

while i >= 0:
    print(' ' * i + '*' * j + ' ' * i)