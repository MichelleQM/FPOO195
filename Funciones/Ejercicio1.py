def total_factura(cantidad_sin_iva, porcentaje=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje / 100)
    return total

total_factura_iva = total_factura(100,16)
print("Total de la factura con un IVA del (16%) es de:", total_factura_iva)

total_factura_iva_default = total_factura(100)
print("Total de la factura con IVA (21% por defecto) es de: ", total_factura_iva_default)