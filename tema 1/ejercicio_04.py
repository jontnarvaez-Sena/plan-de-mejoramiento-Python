"""
Entrada: kilómetros recorridos y litros consumidos. Proceso: distancia / litros. Salida: kilómetros por litro. El enunciado supone que los litros son mayores que cero.
"""

distancia = float(input("Ingrese los kilómetros recorridos: "))
litros = float(input("Ingrese los litros consumidos: "))
consumo = distancia / litros
print("Kilómetros por litro:", consumo)
