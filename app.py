import random
import sys
import time

vida_jugador = 100
vida_monstruo = 100
pociones = 3
turno = 1

# En GitHub Actions se juega automáticamente.
modo_automatico = not sys.stdin.isatty()

print("=" * 40)
print("     BATALLA CONTRA EL MONSTRUO")
print("=" * 40)

nombre = "Roberto"

if not modo_automatico:
    nombre = input("Escribe tu nombre: ").strip() or "Jugador"

print(f"\n¡Bienvenido, {nombre}!")
print("Derrota al monstruo antes de perder toda tu vida.")
print("Tienes 3 pociones para recuperar salud.")

if modo_automatico:
    print("\nModo automático para mostrar el juego en GitHub Actions.")

while vida_jugador > 0 and vida_monstruo > 0:
    print("\n" + "=" * 40)
    print(f"TURNO {turno}")
    print(f"{nombre}: {vida_jugador}/100 de vida")
    print(f"Monstruo: {vida_monstruo}/100 de vida")
    print(f"Pociones disponibles: {pociones}")
    print("=" * 40)

    print("1. Atacar")
    print("2. Usar poción (+30 de vida)")
    print("3. Defenderse (reduce el siguiente daño)")

    opcion = ""

    if modo_automatico:
        opcion = "1"

        if vida_jugador <= 40 and pociones > 0:
            opcion = "2"

        print(f"Opción elegida: {opcion}")
    else:
        opcion = input("Elige una opción: ").strip()

    defendiendo = False

    if opcion == "1":
        ataque = random.randint(15, 25)

        if random.randint(1, 100) <= 25:
            ataque *= 2
            print("\n¡GOLPE CRÍTICO!")

        vida_monstruo = max(0, vida_monstruo - ataque)
        print(f"\nAtacaste al monstruo y causaste {ataque} de daño.")

    elif opcion == "2":
        if pociones == 0:
            print("\n¡Ya no tienes pociones! Elige otra acción.")
            continue

        if vida_jugador == 100:
            print("\nTu vida está completa. Elige otra acción.")
            continue

        recuperacion = min(30, 100 - vida_jugador)
        vida_jugador += recuperacion
        pociones -= 1

        print(f"\nUsaste una poción y recuperaste {recuperacion} de vida.")

    elif opcion == "3":
        defendiendo = True
        print("\n¡Te preparaste para bloquear el ataque!")

    else:
        print("\nOpción inválida. Escribe 1, 2 o 3.")
        continue

    if vida_monstruo > 0:
        ataque_monstruo = random.randint(10, 20)

        if defendiendo:
            ataque_monstruo = max(1, ataque_monstruo // 3)

        vida_jugador = max(0, vida_jugador - ataque_monstruo)

        print(f"El monstruo te atacó y causó {ataque_monstruo} de daño.")

    turno += 1

    if not modo_automatico:
        time.sleep(0.8)

print("\n" + "=" * 40)

if vida_jugador > 0:
    print(f"¡GANASTE, {nombre}!")
    print("Derrotaste al monstruo.")
else:
    print(f"¡PERDISTE, {nombre}!")
    print("El monstruo ganó esta batalla.")

print(f"Turnos jugados: {turno - 1}")
print(f"Vida restante: {vida_jugador}")
print("=" * 40)

if not modo_automatico:
    input("\nPresiona Enter para salir...")