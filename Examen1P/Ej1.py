palabra = input("Introduce una palabra: ")

letras = [(i+1, letra)for i, letra in enumerate(palabra)]
print("Las letras que tiene tu palabra son: ")

for letra in letras:
    print("Letra",letra)