libros = []
def libro_exist():
    if libros:
        return True
    else:
        return False

class Libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def agregar(self,libro):
        libros.append(libro)

    def eliminar(self, nombre):
        delete = False
        for libro in libros:
            if libro.titulo == nombre:
                del libros[libros.index(libro)]
                delete = True
                break
        if not delete:
            print("El libro no existe")

libro1 = Libro('Robinson Crusoe', 'Daniel Defoe', '1719')

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
            if libro_exist():
                print("\n"+"--"*10+" LIBROS EXISTENTES "+"--"*10)
                for libro in libros:
                    print(f"Nombre: {libro.titulo} | Autor: {libro.autor} | Año: {libro.ano}")
            else:
                print("No hay libros")

        case "3":
            if libro_exist():
                while True:
                    try:
                        titulo_delete = input("\nIngrese el titulo del libro a eliminar: ")
                        libro1.eliminar(titulo_delete)
                    except Exception as e:
                        print(f"Error inesperado: {e}")


        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")