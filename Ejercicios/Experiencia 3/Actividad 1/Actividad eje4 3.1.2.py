# Diccionario para almacenar los usuarios y sus contraseñas
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = input("Ingrese nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre de usuario.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        usuarios[nombre_usuario] = contraseña
        print("Usuario registrado con éxito.")

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Error: nombre de usuario o contraseña incorrectos.")

# Función para eliminar un usuario
def eliminar_usuario():
    nombre_usuario = input("Ingrese nombre de usuario a eliminar: ")
    if nombre_usuario in usuarios:
        contraseña = input("Ingrese la contraseña para confirmar: ")
        if usuarios[nombre_usuario] == contraseña:
            del usuarios[nombre_usuario]
            print("Usuario eliminado con éxito.")
        else:
            print("Error: contraseña incorrecta.")
    else:
        print("Error: el usuario no existe.")

# Función para mostrar el menú
def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
mostrar_menu()
