import random
import string

class generadorContrasena():

    def generadorcontra(length=8, include_uppercase=False, include_special_chars=False):
        chars = string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_special_chars:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

