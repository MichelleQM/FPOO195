class Personajes:
    
    #atributo de personaje
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    
    #Metodos del personaje 
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.nombre + "esta corriendo")
        else:
            print("el personaje"+ self.nombre + "no esta corriendo")
            
            
    def lazarGranada(self):
        print(self.nombre+" Pego una granada")
        