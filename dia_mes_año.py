def solicitar_fecha():
    while True:
        try:
            dia = int(input("Por favor, ingresa el día (1-31): "))
            mes = int(input("Por favor, ingresa el mes (1-12): "))
            año = int(input("Por favor, ingresa el año: "))
            return dia, mes, año
        except ValueError:
            print("Por favor, ingresa números válidos.")

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
def dias_en_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes == 2:
        if es_bisiesto(año):
            return 29
        else:
            return 28
    else:
        return 30
def es_fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, año):
        return False
    return True

def main():
    dia, mes, año = solicitar_fecha()
    if es_fecha_valida(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")

if __name__ == "__main__":
    main()