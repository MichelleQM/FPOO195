peso_payaso= 112
peso_muñeca= 75

num_payasos= int(input('Introduce el número de payasos del paquete: '))
num_muñecas= int(input('Introduce el número de muñecas del paquete: '))

peso_final = num_payasos * peso_payaso + num_muñecas * peso_muñeca

print('El peso final del paquete será de', peso_final,'en gramos')