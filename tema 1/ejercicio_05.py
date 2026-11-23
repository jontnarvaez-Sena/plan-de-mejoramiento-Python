"""
Entrada: tarifa fija, costo por unidad y unidades utilizadas. Proceso: tarifa fija + costo por unidad × unidades. Salida: total.
"""

tarifa_fija = float(input("Ingrese la tarifa fija: "))
costo_unidad = float(input("Ingrese el costo por unidad: "))
unidades = float(input("Ingrese las unidades utilizadas: "))
total = tarifa_fija + costo_unidad * unidades
print("Valor total del servicio:", total)
