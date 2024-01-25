
# Practica2: Sintaxis Pyton 

#1. Comentario 

#soy un comentario de 1 linea 
'''soy un 
comentario 
de 
varias lineas 
'''
#2. cadenas 
"""print('soy una cadena')
print("soy otra cadena")"""

a= 'mi banda \n favorita' #\n para soltos de linea 
b= "es grupo marrano"

print(a+b) #concatenar una cadena 
print(a,b)

print(len(a))#cuenta los caracteres 

#cuenta y corta cadenas en base a su posicion
print(b[2:5])
print(b[:5])
print(b[2:])

#3. Variables
#ninguna variable puede comenzar con numeros  

x= 5
y= "john"
x= 4.6
z=3.2

print(x)
print(y)

print(type(x))
print(type(y))
print(type(z))

x= int(3)
y= str("3")
z= float(3.2)

import random
numero= random.randrange(1,15)
print(numero)

#4. Solicitud de datos 
var1= input("introduce cualquier dato")
var2= str( input("Introduce cadenas"))
var3= int( input("Introduce solo enteros"))
var4= float( input("Introduce numeros decimales"))

print(var1, var2, var3, var4)

#5. Boolenas, Operadores de comparacion y logica 
print(10 > 9) #mayor que 
print(10 == 9) #iguala un valor 
print(10 < 9) #menor que 
print(10 >= 9) #mayor igual que 
print(10 != 9)#diferente de
print(10 <= 9) #menor igual que 


X= 1

print(x < 5 and x < 10) #true 
print(x < 5 or x < 10) #false 
print(not(x < 5 and x < 10)) #comparacion de las opraciones

print(x < 5 & x < 10)
print(x < 5 | x < 10)
print(not(x < 5 & x < 10))

