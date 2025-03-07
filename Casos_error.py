import unittest
from gestor_notas import GestorNotas
from usuario import Usuario
from nota import Nota

class TestCasosError(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorNotas()
        self.usuario = self.gestor.crear_cuenta("juan", "1234")
        self.gestor.iniciar_sesion("juan", "1234")

    # CREAR NOTA
    def test_crear_nota_sin_titulo(self):
        nota = self.usuario.crear_nota("", "Sin título", "Trabajo")
        self.assertIsNone(nota)

    def test_crear_nota_sin_contenido(self):
        nota = self.usuario.crear_nota("Titulo", "", "Trabajo")
        self.assertIsNone(nota)

    def test_crear_nota_categoria_invalida(self):
        nota = self.usuario.crear_nota("Titulo", "Contenido", "")
        self.assertIsNone(nota)

    # EDITAR NOTA
    def test_editar_nota_no_existente(self):
        resultado = self.usuario.editar_nota("Inexistente", "Nuevo contenido")
        self.assertFalse(resultado)

    def test_editar_nota_sin_contenido(self):
        self.usuario.crear_nota("Proyecto", "Avance", "Trabajo")
        resultado = self.usuario.editar_nota("Proyecto", "")
        self.assertFalse(resultado)

    def test_editar_nota_titulo_vacio(self):
        resultado = self.usuario.editar_nota("", "Nuevo contenido")
        self.assertFalse(resultado)

    # ELIMINAR NOTA
    def test_eliminar_nota_no_existente(self):
        resultado = self.usuario.eliminar_nota("Inexistente")
        self.assertFalse(resultado)

    def test_eliminar_nota_sin_titulo(self):
        resultado = self.usuario.eliminar_nota("")
        self.assertFalse(resultado)

    def test_eliminar_nota_ya_eliminada(self):
        self.usuario.crear_nota("Tarea", "Hacer informe", "Trabajo")
        self.usuario.eliminar_nota("Tarea")
        resultado = self.usuario.eliminar_nota("Tarea")  # Intentar eliminarla de nuevo
        self.assertFalse(resultado)

    # INICIAR SESIÓN
    def test_iniciar_sesion_contrasena_incorrecta(self):
        resultado = self.gestor.iniciar_sesion("juan", "incorrecta")
        self.assertFalse(resultado)

    def test_iniciar_sesion_usuario_inexistente(self):
        resultado = self.gestor.iniciar_sesion("pedro", "1234")
        self.assertFalse(resultado)

    def test_iniciar_sesion_sin_credenciales(self):
        resultado = self.gestor.iniciar_sesion("", "")
        self.assertFalse(resultado)

    # CREAR CUENTA
    def test_crear_cuenta_usuario_existente(self):
        resultado = self.gestor.crear_cuenta("juan", "abcd")
        self.assertIsNone(resultado)

    def test_crear_cuenta_sin_usuario(self):
        resultado = self.gestor.crear_cuenta("", "abcd")
        self.assertIsNone(resultado)

    def test_crear_cuenta_sin_contrasena(self):
        resultado = self.gestor.crear_cuenta("luis", "")
        self.assertIsNone(resultado)

    # CAMBIAR CONTRASEÑA
    def test_cambiar_contrasena_usuario_inexistente(self):
        resultado = self.gestor.cambiar_contrasena("pepe", "4321", "nuevo")
        self.assertFalse(resultado)

    def test_cambiar_contrasena_misma_clave(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "1234")
        self.assertFalse(resultado)

    def test_cambiar_contrasena_sin_nueva(self):
        resultado = self.gestor.cambiar_contrasena("juan", "1234", "")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
