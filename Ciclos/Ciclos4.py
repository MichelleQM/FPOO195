numero = int(input("Introduce un numero que determine la altura: "))

for i in range(1, numero + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


