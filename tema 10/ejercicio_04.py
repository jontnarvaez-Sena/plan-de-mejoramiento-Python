promedio = float(input("Ingrese el promedio: "))
matricula = input("¿Tiene matricula activa? (si/no): ")

if promedio >= 4.5 and matricula == "si":
    print("Cumple los requisitos preliminares para la beca")
else:
    print("No cumple los requisitos preliminares")