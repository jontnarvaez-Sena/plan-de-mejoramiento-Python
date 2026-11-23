"""
Entrada: número de páginas y precio por página. Proceso: multiplicar. Salida: costo de impresión.
"""

paginas = int(input("Ingrese el número de páginas: "))
precio = float(input("Ingrese el precio por página: "))
costo = paginas * precio
print("Costo de impresión:", costo)
