usuario = input("Ingrese el nombre de usuario: ")

if usuario == "admin":
    autorizacion = input("¿Tiene autorizacion vigente? (si/no): ")

    if autorizacion == "si":
        print("Acceso permitido")
    else:
        print("Acceso denegado")
else:
    print("Usuario no autorizado")
