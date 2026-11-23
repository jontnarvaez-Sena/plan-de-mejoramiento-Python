elementos = int(input("Ingrese la cantidad de elementos: "))

personas = int(input("Ingrese el numero de personas: "))

recibe = elementos // personas

sobran = elementos % personas

print("REPARTICION DE ELEMENTOS")
print("Cantidad de elementos:", elementos)
print("Numero de personas:", personas)
print("Elementos por persona:", recibe)
print("Elementos sobrantes:", sobran)