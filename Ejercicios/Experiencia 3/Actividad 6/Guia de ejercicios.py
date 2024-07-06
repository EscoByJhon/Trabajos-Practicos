# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números con validación de división por cero
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# Función para validar que la entrada sea un número
def validar_entrada(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            # Intentamos convertir la entrada a float
            valor = float(entrada)
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def ejecutar():
    print("Calculadora Básica")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = int(validar_entrada("Elige una opción (1/2/3/4): "))
    if opcion in [1, 2, 3, 4]:
        num1 = validar_entrada("Ingresa el primer número: ")
        num2 = validar_entrada("Ingresa el segundo número: ")
        
        if opcion == 1:
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opción no válida")

ejecutar()

