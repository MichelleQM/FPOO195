import random
import string
import re

class clase:
    def GeneraContrasena(self, length, include_uppercase=False, include_special=False):
        # se determina si la contrasena incluye mayusculas y caracter especial
        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_special:
            characters += string.punctuation

        # retorna el valor de la contra generada 
        return ''.join(random.choice(characters) for _ in range(length))
    
    #Metodo para la verificacion de la contrasena en donde evalua la longitud, si incluye mayusculas o algun caracter especial
    def VerificaFortalezaContrasena(self, contraseña):
        if len(contraseña) < 12:
            return "Se recomiendan al menos 12 caracteres de longitud."
        
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?/~]', contraseña):
            return "Se recomienda al menos algun caracter de tipo especial"
        
        if not re.search(r'[A-Z]', contraseña):
            return "Se recomienda al menos el uso de una letra mayuscula"
        
        return "Tu contrasena es lo duficientemente fuerte"