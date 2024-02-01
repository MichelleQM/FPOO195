def suma(*numero):
    resultado= sum (numero)
    print("suma: ", resultado)
suma(1,2,3,4)

#suma librerias 
import math

def area_cuadrado(lado):
    return lado**2

def main():
    lado_cuadrado=float(input("Ingrese valor de lados: "))
    area_resultado= area_cuadrado(lado_cuadrado)
    
    print(f"area del cuadrado: {area_resultado}")