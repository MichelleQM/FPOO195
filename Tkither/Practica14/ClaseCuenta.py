class Cuenta:
    def __init__(self, numero_cuenta, titular, edad, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, monto):
        self.saldo += monto

    def retirar_efectivo(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def transferir(self, cuenta_destino, monto):
        if self.saldo >= monto:
            self.retirar_efectivo(monto)
            cuenta_destino.ingresar_efectivo(monto)
            return True
        else:
            return False


