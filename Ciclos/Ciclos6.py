saldo = 0
while True:
    operacion = input("Ingrese una operación (D para depósito, R para retiro): ")
    if operacion == "":
        break
    monto = int(input("Ingrese el monto: "))
    if operacion == "D":
        saldo += monto
    elif operacion == "R":
        saldo -= monto
    print(f"Operación: {operacion} {monto}. Saldo actual: {saldo}")
print(f"Saldo final: {saldo}")