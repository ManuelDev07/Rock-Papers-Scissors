#Juego: Piedra, Papel o Tijeras.
import random

while True:

    print("""
            Bienvenid@!
---------------------------------------
    Juego: Piedra, Papel o Tijeras.
---------------------------------------
Menú de juego:
1.- Para Comenzar a Jugar
2.- Para Salir""")


    while True:
        try:
            opcion = int(input('¿Que desea realizar? '))
            break
        except ValueError:
            print("""
            ERROR! debe ingresar un NUMERO de acuerdo al menu de juego...
            """)

    if opcion == 1:
        while True:
            try:
                usuario = input("Su turno. (piedra, papel o tijeras): ").lower()
                break
            except ValueError:
                print("""
                Valor incorrecto! Intente de nuevo
                """)
 

        compu = random.choice(['piedra', "papel", "tijeras"])
        print(f"El computador eligio: {compu}") 
        print()

        if usuario == 'piedra':
            if compu == 'piedra':
                print("Es un Empate!")
            elif compu == "tijeras":
                print("Ganaste!!!")
            else:
                print("Perdiste :(")
        elif usuario == 'papel':
            if compu == 'papel':
                print("Es un Empate!")
            elif compu == "piedra":
                print("Ganaste!!!")
            else:
                print("Perdiste :(")
        elif usuario == 'tijeras':
            if compu == 'tijeras':
                print("Es un Empate!")
            elif compu == "papel":
                print("Ganaste!!!")
            else:
                print("Perdiste :(")
        else:
            print("""
            ERROR! Opcion incorrecta! Intenta de nuevo...
            """)

    elif opcion == 2:
        print("Hasta Pronto! ")
        break
    else:
        print("""
        ERROR! Opcion incorrecta! Intenta de nuevo...
        """)
