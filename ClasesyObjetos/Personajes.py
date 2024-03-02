class Personajes:
    
    #Declaramos el constructor para crear los objetos 
    def __init__(self,esp,nom,alt,pen):
        self.__especie = esp 
        self.__nombre = nom
        self.__altura = alt
        self.__pensar = pen
    
    def setNombre(self, nx):
        self.__nombre = nx
        
    def getNombre(self):
        return self.__nombre
        
    
    #Metodos del personaje 
    def pensar(self):
        print("Tu personaje"+self.__nombre+"esta pensando")
            
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.__nombre + "esta corriendo")
        else:
            print("el personaje"+ self.__nombre + "no esta corriendo")
            
            
    def lazarGranada(self):
        print(self.__nombre+" Pego una granada")
        