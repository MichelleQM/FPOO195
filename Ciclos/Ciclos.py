contador = 1

while contador < 5:
    if contador == 3:
        break
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado normalmante")
    

#uso continue
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)
else:
    print("El bucle ha terminado normalmante")

#ciclo for 
palabra = input("Ingrese una palabra: ")
contador_vocales = 0
for letras in palabra:
    if letras.lower() in "aeiou":
        contador_vocales += 1
print(f"La palabra '{palabra}' tiene {contador_vocales} vocal(es).")
    
    
#este programa va a calcular a suma de los numeros pares del 1 al 10 
suma = 0
for num in range(1,11):
    if num % 2 == 0:
        suma += num
print(f"La suma de los numeros para del 1 al 10 es: {suma}")
