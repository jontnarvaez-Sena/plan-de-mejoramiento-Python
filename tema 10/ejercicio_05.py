compra = float(input("Ingrese el valor de la compra: "))
fidelizacion = input("¿Pertenece al programa de fidelizacion? (si/no): ")

if compra > 150000 or fidelizacion == "si":
    print("Felicitaciones, aplica para la promocion")
else:
    print("No aplica para la promocion")