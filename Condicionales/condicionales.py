z= 4
if z % 2 == 0:
    print("z is even")
    
    
#if else 
z= int(input("Ingresa un numero, entero: "))
if z % 2 == 0:
    print("z es par")
else:
    print("z es impar")
    
#elif-else
room= "bed"
area= 14.0
if room == "kit":
    print("Looking around in the kitchen")
elif room == "bed":
    print("Loking around in the bedroom")
else:
    print("looking around elsewhere")
    if area > 15:
        print("Big place!")
    else:
        print("Pretty small")

