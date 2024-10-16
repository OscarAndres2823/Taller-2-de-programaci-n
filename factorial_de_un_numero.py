# Solicita al usuario un número entero positivo
n = int(input("Ingresa un número entero positivo: "))

# Verifica que el número ingresado sea positivo
if n < 0:
    print("Por favor, ingresa un número entero positivo.")
elif n == 0:
    # El factorial de 0 es 1
    factorial = 1
else:
    # Inicializa el resultado del factorial en 1
    factorial = 1
    
    # Usa un ciclo for para calcular el factorial
    for i in range(1, n + 1):
        factorial *= i

    # Muestra el resultado
    print(f"El factorial de {n} es: {factorial}")
