def iniciar_sesion(usuarios, contrasenas):
    while True:
        print("\nMenú de inicio de sesión:")
        print("1) Iniciar sesión")
        print("2) Registrar usuario")
        print("3) Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            
            if usuario in usuarios:
                index = usuarios.index(usuario)
                if contrasena == contrasenas[index]:
                    print(f"\n¡Bienvenido, {usuario}!")
                    return index + 1  # Retorna el número de usuario (1, 2, 3)
                else:
                    print("Contraseña incorrecta. Inténtelo nuevamente.")
            else:
                print("Usuario no registrado. Registre un usuario primero.")
        
        elif opcion == '2':
            for i in range(len(usuarios)):
                if usuarios[i] is None:
                    usuario = input("Ingrese un nuevo usuario: ")
                    contrasena = input("Ingrese una contraseña: ")
                    
                    usuarios[i] = usuario
                    contrasenas[i] = contrasena
                    print(f"Usuario {usuario} registrado correctamente.")
                    break
            else:
                print("Ya se han registrado el máximo de usuarios.")
        
        elif opcion == '3':
            print("¡Hasta luego!")
            return 0
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

def menu_principal(usuario_index):
    opciones_menu = ["Realizar llamada", "Enviar correo electrónico", "Cerrar sesión"]
    
    while True:
        print(f"\nMenú de opciones para {usuarios[usuario_index - 1]}:")
        for i, opcion in enumerate(opciones_menu, start=1):
            print(f"{i}) {opcion}")
        
        opcion = input(f"Seleccione una opción (1/2/3): ")
        
        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                raise ValueError("Opción fuera de rango.")
            
            if opcion == 1:
                realizar_llamada()
            elif opcion == 2:
                enviar_correo()
            elif opcion == 3:
                print(f"Cerrando sesión de {usuarios[usuario_index - 1]}...")
                return
        
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")

def realizar_llamada():
    while True:
        celular = input("Ingrese el número de celular (9 dígitos, empieza con 9): ")
        
        if len(celular) == 9 and celular.isdigit() and celular[0] == '9':
            print(f"Llamando al número {celular}...")
            break
        else:
            print("Número de celular inválido. Inténtelo nuevamente.")

def enviar_correo():
    while True:
        correo = input("Ingrese su correo electrónico: ")
        
        if '@' in correo:
            mensaje = input("Ingrese el mensaje a enviar: ")
            print(f"Enviando correo a {correo}: '{mensaje}'")
            break
        else:
            print("Correo electrónico inválido. Debe contener al menos un '@'. Inténtelo nuevamente.")

# Variables de usuarios y contraseñas
usuarios = [None, None, None]
contrasenas = [None, None, None]

# Ejecución del programa
while True:
    usuario_index = iniciar_sesion(usuarios, contrasenas)
    if usuario_index != 0:
        menu_principal(usuario_index)
    else:
        break
