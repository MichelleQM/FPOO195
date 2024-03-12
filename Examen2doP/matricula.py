import string
import re

class matricula:
    def __init__(self, nombre, apellidoP, apellidoM, nacimiento, carrera):
        self.__nombre=nombre
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__nacimiento=nacimiento
        self.__carrera=carrera
        
    def datosMaricula(self, creacionMatricula):
        