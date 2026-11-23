ahorrado = float(input("Ingrese la cantidad ahorrada: "))

meta = float(input("Ingrese la meta de ahorro: "))

if ahorrado >= meta:
    print("Felicitaciones, alcanzo su meta de ahorro")
else:
    falta = meta - ahorrado
    print("Todavia no alcanza la meta de ahorro")
    print("El dinero que le falta es:", falta)
    