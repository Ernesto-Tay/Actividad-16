from bdb import Breakpoint

libros = []
class Libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def agregar(self,libro):
        libros.append(libro)

    def mostrar(self):
        if not libros:
            print("No hay libros aún")
        else:
            print("--"*10 + " LIBROS " + "--"*10)
            for libro in libros:
                print(f"Nombre: {libro['titulo']}. Autor: {libro['autor']}. Año: {libro['ano']}")

    def eliminar(self, nombre):
        for libro in libros:
            if libro['titulo'] == nombre:
                del libros[libros.index(libro)]

while True:
    print("\n\nSISTEMA DE LIBROS\n1. Agregar libros\n2. Mostrar lista de libros\n3. Eliminar libro\n4. Salir")
    select = input("Seleccione una opción")
    match select:
        case "1":
            while True:
                try:
                    cant = int(input("¿Cuántos libros va a ingresar?: "))
                    if cant <= 0:
                        print("La cantidad debe ser superior a 0")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero")
                except Exception as e:
                    print(f"Error inesperado: {e}")

            for i in range(cant):
                while True:
                    try:
                        titulo = input("\nIngrese el titulo del libro: ")
                        autor = input("Ingrese el autor del libro: ")
                        ano = int(input("Ingrese el año de lanzamiento del libro: "))
                        if autor.isalpha() and 1000<ano<2026:
                            break
                        else:
                            if not autor.isalpha():
                                print("El nombre del autor no puede tener letras")
                            elif ano < 1000 or ano > 2026:
                                print("Ingrese una fecha de lanzamiento razonable")
                    except ValueError:
                        print("Ingrese números enteros en la entrada del año")
                    except Exception as e:
                        print(f"Error inesperado: {e}")
                libro = Libro(titulo, autor, ano)
                libro.agregar(libro)

        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case _:
            print("Opción inválida, intente nuevamente")