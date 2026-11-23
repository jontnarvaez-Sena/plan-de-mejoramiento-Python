instructora = input("Es instructora? (True/False): ")

autorizacion = input("Tiene autorizacion? (True/False): ")

instructora = instructora == "True"

autorizacion = autorizacion == "True"

resultado = instructora or autorizacion

print("VALIDACION DE ACCESO")
print("Puede acceder al recurso:", resultado)