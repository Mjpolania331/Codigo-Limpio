class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena
        self.notas = []

    def crear_nota(self, titulo, contenido, categoria):
        nota = Nota(titulo, contenido, categoria)
        self.notas.append(nota)

    def editar_nota(self, titulo, nuevo_contenido):
        for nota in self.notas:
            if nota.titulo == titulo:
                nota.contenido = nuevo_contenido
                return True
        return False

    def eliminar_nota(self, titulo):
        self.notas = [nota for nota in self.notas if nota.titulo != titulo]

    def mostrar_notas(self):
        for nota in self.notas:
            print(nota)
            print("-" * 30)
