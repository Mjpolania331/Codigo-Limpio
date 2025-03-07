from gestor_notas import GestorNotas
from utilidades import pedir_datos_nota

def menu():
    gestor = GestorNotas()

    while True:
        print("\n enú Gestor de Notas ")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            contrasena = input("Contraseña: ")
            if gestor.crear_cuenta(nombre, contrasena):
                print("Cuenta creada exitosamente.")
            else:
                print("El usuario ya existe.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            contrasena = input("Contraseña: ")
            usuario = gestor.iniciar_sesion(nombre, contrasena)

            if usuario:
                print(f"\nBienvenido, {nombre}")
                while True:
                    print("\n Menú de Usuario ")
                    print("1. Crear nota")
                    print("2. Editar nota")
                    print("3. Eliminar nota")
                    print("4. Mostrar mis notas")
                    print("5. Cambiar contraseña")
                    print("6. Cerrar sesión")
                    subopcion = input("Elige una opción: ")

                    if subopcion == "1":
                        titulo, contenido, categoria = pedir_datos_nota()
                        usuario.crear_nota(titulo, contenido, categoria)
                        print("Nota creada.")

                    elif subopcion == "2":
                        titulo = input("Título de la nota a editar: ")
                        nuevo_contenido = input("Nuevo contenido: ")
                        if usuario.editar_nota(titulo, nuevo_contenido):
                            print("Nota editada.")
                        else:
                            print("Nota no encontrada.")

                    elif subopcion == "3":
                        titulo = input("Título de la nota a eliminar: ")
                        usuario.eliminar_nota(titulo)
                        print("Nota eliminada.")

                    elif subopcion == "4":
                        print("\nTus notas:")
                        usuario.mostrar_notas()

                    elif subopcion == "5":
                        nueva_contrasena = input("Nueva contraseña: ")
                        gestor.cambiar_contrasena(nombre, nueva_contrasena)
                        print("Contraseña actualizada.")

                    elif subopcion == "6":
                        print("Sesión cerrada.")
                        break

                    else:
                        print("Opción inválida.")

            else:
                print("Credenciales incorrectas.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
