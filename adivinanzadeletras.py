# Letra secreta predefinida
letra_secreta = "A"

# Solicita al usuario que adivine la letra
letra_usuario = input("Adivina la letra secreta (una sola letra): ").upper()

# Usa match para verificar si el usuario adivinó la letra secreta
match letra_usuario:
    case "A":
        print("¡Felicidades! Adivinaste la letra secreta.")
    case _:
        print("Lo siento, esa no es la letra secreta.")
