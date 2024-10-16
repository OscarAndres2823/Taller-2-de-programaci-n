def verificar_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

def main():
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        print(verificar_edad(edad))
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")

if __name__ == "__main__":
    main()