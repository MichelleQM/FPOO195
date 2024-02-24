#importacion de la clase (* se usa para indicar todo) 
from Personajes import *
from Armas import *

#creamos las instancias para las acciones de cada personaje (Se crea un objeto de las clases creadas)
spartan = Personajes()
Arma = Armas()

#Usamos los atributos 
print(spartan.nombre)
print(spartan.especie) 
print(spartan.altura)

#Usamos los metodos del spartan 
spartan.correr(False)
spartan.lazarGranada()

#usamos metodos del arma
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)