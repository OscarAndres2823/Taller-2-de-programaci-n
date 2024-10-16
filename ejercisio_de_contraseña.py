def solicitar_contraseña():
    while True:
        contraseña = input("Por favor, ingresa una contraseña: ")
        if verificar_contraseña(contraseña):
            return contraseña
        else:
            print("Contraseña inválida. Por favor, inténtalo de nuevo.")

def verificar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    return True

def main():
    contraseña = solicitar_contraseña()
    print("Contraseña válida")

if __name__ == "__main__":
    main()