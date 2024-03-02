#importacion de la clase (* se usa para indicar todo) 
from Personajes import *
from Armas import *

#solicitamos datos Spartan
print("Datos del Heroe")
nombreS= input("Escribe el nombre de tu Spartan: ")
especieS= input("Escribe la especie de tu Spartan: ")
alturaS= float(input("Escribe la estatuta de tu Spartan: "))
pensamientoS = input("")
print("")

#solicitamos datos Nemesis 
print("Datos del Villano")
nombreN= input("Escribe el nombre de tu Nemesis: ")
especieN= input("Escribe la especie de tu Nemesis: ")
alturaN= float(input("Escribe la estatuta de tu Nemesis: "))
pensamientoN= input("")
print("")

#creamos las instancias para las acciones de cada personaje (Se crea un objeto de las clases creadas)
Spartan= Personajes(especieS,nombreS,alturaS,pensamientoS)
Nemesis= Personajes(especieN,nombreN,alturaN,pensamientoN)
Arma = Armas()

#se fijan los atributos para el spartan
print(Spartan.getnombre())
print(Spartan.getespecie())
print(Spartan.getaltura())
print(Spartan.getpensamiento())

#se fijan los atributos para el nemesis 
print(Nemesis.getnombre())
print(Nemesis.getespecie())
print(Nemesis.getaltura())
print(Nemesis.getpensamiento())

#usamos los metodos del spartan
Spartan.correr(False)
Spartan.lanzarGranada()
Spartan.pensamiento(False)

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
Arma.seleccionarArma(Spartan.getNombre)
Arma.recargarArma(65)