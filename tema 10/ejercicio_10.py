lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print("Las longitudes pueden formar un triangulo")
    else:
        print("Las longitudes no pueden formar un triangulo")

else:
    print("Los lados deben ser mayores que cero")
