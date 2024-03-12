import string
import re
import random

class matricula:
    def __init__(self, nombre, apellidoP, apellidoM, nacimiento, carrera, curso):
        self.__nombre=nombre
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__nacimiento=nacimiento
        self.__carrera=carrera
        self.__curso='2024'
        self.__numAleatorio1 = random(0,99)
        self.__numAleatorio2 = random(0,99)
        
    def datosMaricula(self, nombre, apellidoP, apellidoM, nacimiento, carrera,curso, numAleatorio1, numAleatorio2):
        matricula = nombre[1] + apellidoP[:2] + apellidoM[:2] + str(nacimiento)[-2:] + str(curso)[-2:] + carrera[:2]+ str(numAleatorio1) + str(numAleatorio2)

