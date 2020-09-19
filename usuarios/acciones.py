import usuarios.usuario as user
import notas.acciones as notaAccion

class Acciones:
    def registro(self):
        print("\nOk, Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una contraseña: ")

        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nGenial, {registro[1].nombre} te has registrado correctamente")
        else:
            print("\nHa habido un error durante el registro...")
    
    def login(self):
        print("\nVale, vamos a crear una cuenta nueva")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce una contraseña: ")

            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te registraste el día {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, vuelvelo a intentar")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - crear: Crear nueva nota.
        - mostrar: Mostrar tus notas.
        - eliminar: Eliminar nota.
        - salir
        """)

        accion = input("¿Qué quieres hacer?: ")
        note = notaAccion.Acciones()

        if accion == "crear":
            note.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            note.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            note.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok, Hasta pronto {usuario[1]}!")
            exit()