radio= int(input("Ingresa el radio del circulo: "))
altura= int(input("Ingresa la altura del cilindor: "))

import math
def area_circulo(radio):
    area = math.pi * radio **2
    return area

def volumen(radio, altura):
    base= area_circulo(radio)
    volumen = base * altura
    return volumen

area = area_circulo (radio)
print("El area del circulo es: ", area)

volumen_cilindro = volumen(radio, altura)
print("El volumen del cilindro es: ", volumen_cilindro)