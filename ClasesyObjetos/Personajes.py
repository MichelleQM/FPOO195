class Personajes:
    
    #Declaramos el constructor para crear los objetos 
    def __init__(self,esp,nom,alt):
        self.especie = esp 
        self.nombre = nom
        self.altura = alt 
    
    
    #Metodos del personaje 
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.nombre + "esta corriendo")
        else:
            print("el personaje"+ self.nombre + "no esta corriendo")
            
            
    def lazarGranada(self):
        print(self.nombre+" Pego una granada")
        