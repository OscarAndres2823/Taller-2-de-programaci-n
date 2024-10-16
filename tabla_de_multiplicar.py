def solicitar_número():
    while True:
        try:
            número = int(input("Por favor, ingresa un número: "))
            return número
        except ValueError:
            print("Por favor, ingresa un número válido.")

def mostrar_tabla_de_multiplicar(número):
    print(f"Tabla de multiplicar del {número}:")
    for i in range(1, 11):
        print(f"{número} x {i} = {número * i}")

def main():
    número = solicitar_número()
    mostrar_tabla_de_multiplicar(número)

if __name__ == "__main__":
    main()