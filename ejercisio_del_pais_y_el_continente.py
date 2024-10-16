def determinar_continente():
   
    pais = input("Por favor, ingresa el nombre de un país: ").strip().lower()

    if pais in ['canadá', 'estados unidos', 'méxico']:
        print(f"{pais.title()} está en América del Norte.")
    elif pais in ['brasil', 'argentina', 'chile', 'perú', 'colombia']:
        print(f"{pais.title()} está en América del Sur.")
    elif pais in ['españa', 'francia', 'alemania', 'italia', 'reino unido']:
        print(f"{pais.title()} está en Europa.")
    elif pais in ['china', 'japón', 'india', 'corea del sur', 'indonesia']:
        print(f"{pais.title()} está en Asia.")
    elif pais in ['nigeria', 'egipto', 'sudáfrica', 'kenia', 'etiopía']:
        print(f"{pais.title()} está en África.")
    elif pais in ['australia', 'nueva zelanda']:
        print(f"{pais.title()} está en Oceanía.")
    elif pais in ['antártida']:
        print(f"{pais.title()} está en la Antártida.")
    else:
        print("Lo siento, no tengo información sobre ese país.")
        
determinar_continente()
