libros = []
class libro:
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
            print("--"+10 + " LIBROS " + "--"*10)
            for libro in libros:
                print(f"Nombre: {libro['titulo']}. Autor: {libro['autor']}. Año: {libro['ano']}")

    def eliminar(self, nombre):
        for libro in libros:
            if libro['titulo'] == nombre:
                del libros[libros.index(libro)]




