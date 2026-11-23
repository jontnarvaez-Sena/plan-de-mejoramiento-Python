compra = float(input("Ingrese el valor de la compra: "))

if compra >= 100000:
    envio = 0
    print("Su envio es gratis")
else:
    envio = 8000
    print("El costo del envio es de:", envio)

print("RESUMEN DE LA COMPRA")
print("Valor de la compra:", compra)
print("Costo del envio:", envio)