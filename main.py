print("""
Acciones disponibles:
    - registro
    - login
""")

from usuarios import acciones

accion = input("¿Qué quieres hacer?: ")

acciones = acciones.Acciones()

if accion == "registro":
    acciones.registro()
elif accion == "login":
    acciones.login()
else:
    print("Introduce una acción válida, por favor.")