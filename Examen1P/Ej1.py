palabra = input("Introduce una palabra: ")

letras = [letra for letra in palabra]
print("Las letras que tiene tu palabra son: ")

for letra in letras:
    print(letra)