def imprimir_numeros_descendentes():
    while True:
        try:
            num = int(input("Por favor, ingresa un número entero positivo: "))
            if num <= 0:
                print("Por favor, ingresa un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    while num >= 1:
        print(num)
        num -= 1

if __name__ == "__main__":
    imprimir_numeros_descendentes()