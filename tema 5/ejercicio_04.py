
edad = int(input("Ingrese su edad: "))
documento = input("Tiene documento vigente? Escriba True o False: ") == "True"

resultado = False

if edad >= 18:
    if documento:
        resultado = True

print("Es mayor de edad y tiene documento vigente:", resultado)