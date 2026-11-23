nombre = input("Ingrese el nombre de la persona: ")

horas = float(input("Ingrese las horas trabajadas: "))

pago_hora = float(input("Ingrese el pago por hora: "))

total = horas * pago_hora

print("RESUMEN DEL PAGO")
print("Nombre:", nombre)
print("Horas trabajadas:", horas)
print("Pago por hora:", pago_hora)
print("Pago total:", total)