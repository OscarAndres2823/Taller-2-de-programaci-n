def solicitar_números():
    números = []
    while True:
        try:
            número = float(input("Por favor, ingresa un número (ingresa un número negativo para terminar): "))
            if número < 0:
                break
            números.append(número)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return números

def calcular_promedio(números):
    if len(números) == 0:
        return 0
    return sum(números) / len(números)

def main():
    números = solicitar_números()
    if len(números) == 0:
        print("No se ingresaron números positivos.")
    else:
        promedio = calcular_promedio(números)
        print(f"El promedio de los números ingresados es: {promedio}")

if __name__ == "__main__":
    main()