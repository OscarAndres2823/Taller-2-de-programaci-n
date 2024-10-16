def solicitar_calificacion():
    while True:
        try:
            calificacion = float(input("Por favor, ingresa tu calificación (0-100): "))
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def determinar_resultado(calificacion):
    if calificacion >= 60:
        return "Has aprobado"
    else:
        return "Has reprobado"

def main():
    calificacion = solicitar_calificacion()
    resultado = determinar_resultado(calificacion)
    print(resultado)

if __name__ == "__main__":
    main()