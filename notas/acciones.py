import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\n{usuario[1]}, Vamos a crear una nueva nota...")
        
        titulo = input("Introduce un título para tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nLa nota con título {nota.titulo} se ha guardado correctamente!")
        else: 
            print(f"\nHa habido un error al guardar la nota.")

    def mostrar(self, usuario):
        print(f"\nAquí tienes tus notas {usuario[1]}")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n*****************************************")
            print(nota[2])
            print(nota[3])
            print("*****************************************")

    def borrar(self, usuario):
        print(f"\nVamos a borrar notas {usuario[1]}")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")

        else:
            print("No se ha borrado la nota, prueba luego....")