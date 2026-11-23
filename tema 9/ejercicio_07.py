horas = int(input("Ingrese las horas de estacionamiento: "))

if horas <= 2:
    print("El valor del parqueadero es: $3000")
elif horas <= 5:
    print("El valor del parqueadero es: $6000")
else:
    print("El valor del parqueadero es: $10000")
