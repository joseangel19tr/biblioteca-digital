# ============================================
# Sistema de Gestión de Biblioteca Digital
# Versión Final - Interactiva en Consola
# ============================================

class Biblioteca:

    def __init__(self):
        self.usuarios = {}   # {id: nombre}
        self.libros = {}     # {titulo: {"autor": autor, "disponible": True}}

    # =========================
    # Registrar Usuario
    # =========================
    def registrar_usuario(self, id_usuario, nombre):

        self.usuarios[id_usuario] = nombre
        print(f"Usuario '{nombre}' registrado correctamente.")
        return True


    # =========================
    # Registrar Libro
    # =========================
    def registrar_libro(self, titulo, autor):

        if titulo in self.libros:
            print("Error: El libro ya existe.")
            return False

        self.libros[titulo] = {
            "autor": autor,
            "disponible": True
        }

        print(f"Libro '{titulo}' registrado correctamente.")
        return True


    # =========================
    # Prestar Libro
    # =========================
    def prestar_libro(self, id_usuario, titulo):

        if titulo not in self.libros:
            print("Error: El libro no existe.")
            return False

        if id_usuario not in self.usuarios:
            print("Error: Usuario no registrado.")
            return False

        if not self.libros[titulo]["disponible"]:
            print("Error: El libro ya está prestado.")
            return False

        self.libros[titulo]["disponible"] = False
        print(f"Libro '{titulo}' prestado a {self.usuarios[id_usuario]}.")
        return True


    # =========================
    # Devolver Libro
    # =========================
    def devolver_libro(self, titulo):

        if titulo not in self.libros:
            print("Error: El libro no existe.")
            return False

        if self.libros[titulo]["disponible"]:
            print("Aviso: El libro no estaba prestado.")
            return False

        self.libros[titulo]["disponible"] = True
        print(f"Libro '{titulo}' devuelto correctamente.")
        return True


    # =========================
    # Buscar Libro
    # =========================
    def buscar_libro(self, busqueda):

        resultados = [
            t for t, info in self.libros.items()
            if busqueda.lower() in t.lower()
            or busqueda.lower() in info["autor"].lower()
        ]

        if resultados:
            print("\nResultados encontrados:")
            for libro in resultados:
                estado = "Disponible" if self.libros[libro]["disponible"] else "Prestado"
                print(f"- {libro} ({self.libros[libro]['autor']}) - {estado}")
        else:
            print("No se encontraron resultados.")


    # =========================
    # Reporte de Libros Disponibles
    # =========================
    def reporte_disponibles(self):

        disponibles = [
            t for t, info in self.libros.items()
            if info["disponible"]
        ]

        print("\nLibros disponibles:")

        if disponibles:
            for libro in disponibles:
                print(f"- {libro} ({self.libros[libro]['autor']})")
        else:
            print("No hay libros disponibles.")


# ============================================
# MENÚ INTERACTIVO
# ============================================

def mostrar_menu():
    print("\n=================================")
    print("      BIBLIOTECA DIGITAL")
    print("=================================")
    print("1. Registrar usuario")
    print("2. Registrar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro")
    print("6. Ver libros disponibles")
    print("7. Salir")
    print("=================================")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":

    biblioteca = Biblioteca()

    while True:

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # =========================
        # Registrar usuario
        # =========================
        if opcion == "1":

            while True:
                try:
                    id_usuario = input("Ingrese ID del usuario: ")

                    if not id_usuario.strip():
                        print("Error: El ID no puede estar vacío.")
                        continue
                    
                    id_usuario = int(id_usuario)

                    if id_usuario <= 0:
                        print("Error: El ID debe ser mayor que 0 y # positivo.")
                        continue

                    if id_usuario in biblioteca.usuarios:
                        print("Error: El ID ya está registrado.")
                        continue

                    break

                except ValueError:
                    print("Error: El ID debe ser numérico.")

            while True:
                nombre = input("Ingrese nombre del usuario: ")
                if not nombre.strip():
                    print("Error: El nombre no puede estar vacío.")
                else:
                    break

            biblioteca.registrar_usuario(id_usuario, nombre)


        # =========================
        # Registrar libro
        # =========================
        elif opcion == "2":

            while True:
                titulo = input("Ingrese título del libro: ")
                if not titulo.strip():
                    print("Error: El título no puede estar vacío.")
                else:
                    break

            while True:
                autor = input("Ingrese autor del libro: ")
                if not autor.strip():
                    print("Error: El autor no puede estar vacío.")
                else:
                    break

            biblioteca.registrar_libro(titulo, autor)


        # =========================
        # Prestar libro
        # =========================
        elif opcion == "3":

            while True:
                try:
                    id_usuario = int(input("Ingrese ID del usuario: "))
                    break
                except ValueError:
                    print("Error: El ID debe ser numérico.")

            while True:
                titulo = input("Ingrese título del libro: ")
                if not titulo.strip():
                    print("Error: El título no puede estar vacío.")
                else:
                    break

            biblioteca.prestar_libro(id_usuario, titulo)


        # =========================
        # Devolver libro
        # =========================
        elif opcion == "4":

            while True:
                titulo = input("Ingrese título del libro: ")
                if not titulo.strip():
                    print("Error: El título no puede estar vacío.")
                else:
                    break

            biblioteca.devolver_libro(titulo)


        # =========================
        # Buscar libro
        # =========================
        elif opcion == "5":

            while True:
                busqueda = input("Ingrese título o autor a buscar: ")
                if not busqueda.strip():
                    print("Error: No puede estar vacío.")
                else:
                    break

            biblioteca.buscar_libro(busqueda)


        # =========================
        # Reporte
        # =========================
        elif opcion == "6":

            biblioteca.reporte_disponibles()


        # =========================
        # Salir
        # =========================
        elif opcion == "7":

            print("\nSaliendo del sistema...")
            break


        else:

            print("Opción inválida. Intente nuevamente.")