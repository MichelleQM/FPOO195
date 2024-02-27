#importacion de la clase (* se usa para indicar todo) 
from Personajes import *
from Armas import *

#solicitamos datos Spartan
print("Datos del Heroe")
nombreS= input("Escribe el nombre de tu Spartan: ")
especieS= input("Escribe la especie de tu Spartan: ")
alturaS= float(input("Escribe la estatuta de tu Spartan: "))
print("")

#solicitamos datos Nemesis 
print("Datos del Villano")
nombreN= input("Escribe el nombre de tu Nemesis: ")
especieN= input("Escribe la especie de tu Nemesis: ")
alturaN= float(input("Escribe la estatuta de tu Nemesis: "))
print("")

#creamos las instancias para las acciones de cada personaje (Se crea un objeto de las clases creadas)
Spartan= Personajes(especieS,nombreS,alturaS)
Nemesis= Personajes(especieN,nombreN,alturaN)
Arma = Armas()

#Usamos los atributos para Spartan
print("==== EL objeto Spartancontien ====") 
print(Spartan.nombre)
print(Spartan.especie) 
print(Spartan.altura)
print("")

#Usamos los atributos para Nemesis
print("==== EL objeto Spartancontien ====") 
print(Nemesis.nombre)
print(Nemesis.especie) 
print(Nemesis.altura)
print("")

#Usamos los metodos del spartan 
Spartan.correr(False)
Spartan.lazarGranada()

#usamos metodos del arma
Arma.seleccionarArma(Spartan.nombre)
Arma.recargarArma(65)