class Personaje:
    
    #atributo de personaje
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    
    #Metodos del personaje 
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.nombre +"esta corriendo")
        else:
            print("el personaje"+ self.nombre +"no esta corriendo")
            
            
    def lazarGranada(self):
        print(self.nombre+"Pego una granada")
        
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print("Arma recargada al "+ str(cargador)+ "%")
        
#creamos las instancias para las acciones de cada personaje 
spartan = Personaje()
print(spartan.nombre)
print(spartan.especie) 
print(spartan.altura)