porcentaje = float(input("Ingrese el porcentaje de cumplimiento: "))

if porcentaje < 60:
    print("Nivel bajo")
elif porcentaje < 80:
    print("Nivel medio")
elif porcentaje < 95:
    print("Nivel alto")
else:
    print("Nivel excelente")