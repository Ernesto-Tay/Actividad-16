libros = []
class libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def agregar(self):
        libro = {
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano
        }
        libros.append(libro)

    def mostrar(self):
        print("--"+10 + " LIBROS " + "--"*10)
        for libro in libros:
            print(f"Nombre: {libro['titulo']}. Autor: {libro['autor']}. Año: {libro['ano']}")

    def eliminar(self, nombre):
        for libro in libros:
            if libro['titulo'] == nombre:
                del libros[libros.index(libro)]




