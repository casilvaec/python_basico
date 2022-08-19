# Convierte dólares a bolivares
dolares = input("Ingrese cantidad de dólares que desea convertir a bolivares:")
dolares = float(dolares) # Texto ingresado se convierte a valor decimal
valor_bolivar = 6.09 # Valor referencial al 19/08/22
bolivares = dolares * valor_bolivar 
bolivares = round(bolivares, 2) # resultado se acorta a 2 decimales
bolivares = str(bolivares) # Valor se convierte a texto
print("Son $ " + bolivares + " bolivares")