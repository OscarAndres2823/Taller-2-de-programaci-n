def solicitar_longitudes():
    while True:
        try:
            a = float(input("Por favor, ingresa la primera longitud: "))
            b = float(input("Por favor, ingresa la segunda longitud: "))
            c = float(input("Por favor, ingresa la tercera longitud: "))
            return a, b, c
        except ValueError:
            print("Por favor, ingresa números válidos.")

def es_triángulo_válido(a, b, c):
    return a + b > c and a + c > b and b + c > a

def main():
    a, b, c = solicitar_longitudes()
    if es_triángulo_válido(a, b, c):
        print(f"Las longitudes {a}, {b} y {c} pueden formar un triángulo válido.")
    else:
        print(f"Las longitudes {a}, {b} y {c} no pueden formar un triángulo válido.")

if __name__ == "__main__":
    main()