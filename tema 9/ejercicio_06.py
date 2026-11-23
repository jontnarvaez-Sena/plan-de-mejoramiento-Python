numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

operacion = input("Ingrese la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print("El resultado es:", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print("El resultado es:", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print("El resultado es:", resultado)
elif operacion == "/":
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
else:
    print("Operacion no valida")