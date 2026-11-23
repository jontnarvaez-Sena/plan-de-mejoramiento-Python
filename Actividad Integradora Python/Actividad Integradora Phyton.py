
# CALCULO DE INCREMENTO DE PLANES TELIRED

clientes = int(input("Ingrese la cantidad de clientes: "))
plan_actual = int(input("Ingrese el valor del plan actual: "))
plan_nuevo = int(input("Ingrese el valor del nuevo plan: "))

iva_porcentaje = 19

if clientes > 0:

    ingreso_actual = clientes * plan_actual
    ingreso_nuevo = clientes * plan_nuevo

    incremento = ingreso_nuevo - ingreso_actual

    iva_cliente = plan_nuevo * iva_porcentaje / 100
    iva_total = iva_cliente * clientes

    total_cliente = plan_nuevo + iva_cliente
    total_con_iva = ingreso_nuevo + iva_total

    print("----- RESULTADOS TELIRED -----")
    print("Cantidad de clientes:", clientes)
    print("Valor del plan anterior:", plan_actual)
    print("Valor del nuevo plan:", plan_nuevo)
    print("Ingresos con el plan anterior:", ingreso_actual)
    print("Ingresos con el nuevo plan:", ingreso_nuevo)
    print("Incremento mensual:", incremento)
    print("IVA por cliente:", iva_cliente)
    print("IVA total:", iva_total)
    print("Total por cliente con IVA:", total_cliente)
    print("Total mensual con IVA:", total_con_iva)

else:
    print("No hay clientes registrados")
