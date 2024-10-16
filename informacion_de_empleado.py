def solicitar_datos_empleado():
    nombre = input("Por favor, ingresa el nombre del empleado: ")
    apellidos = input("Por favor, ingresa los apellidos del empleado: ")
    telefono = input("Por favor, ingresa el teléfono del empleado: ")
    año_ingreso = int(input("Por favor, ingresa el año de ingreso a la empresa: "))
    edad = int(input("Por favor, ingresa la edad del empleado: "))
    return nombre, apellidos, telefono, año_ingreso, edad

def calcular_antigüedad(año_ingreso):
    from datetime import date
    año_actual = date.today().year
    return año_actual - año_ingreso

def imprimir_datos_empleado(nombre, apellidos, telefono, año_ingreso, edad, antigüedad):
    print("Información del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Teléfono: {telefono}")
    print(f"Antigüedad: {antigüedad} años")
    print(f"Edad: {edad} años")

def main():
    nombre, apellidos, telefono, año_ingreso, edad = solicitar_datos_empleado()
    antigüedad = calcular_antigüedad(año_ingreso)
    imprimir_datos_empleado(nombre, apellidos, telefono, año_ingreso, edad, antigüedad)

if __name__ == "__main__":
    main()