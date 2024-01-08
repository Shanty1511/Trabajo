"""
++++++++++++++++++++++++
+ TORNEO TENIS DE MESA +
++++++++++++++++++++++++
"""
import torneo_tenis_de_mesa 

jugadores_por_categoria = {}

while True:
    print("1. Registrar jugador\n2. Registrar partido\n3. Obtener ganador de cada categoria\n4. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        id_jugador = int(input("Ingrese el ID del jugador: "))
        nombre = input("Ingrese el nombre del jugador: ")
        edad = int(input("Ingrese la edad del jugador: "))
        if 15 <= edad <= 16:
            categoria = "Novato"
        elif 17 <= edad <= 20:
            categoria = "Intermedio"
        else:
            categoria = "Avanzado"
        jugador = torneo_tenis_de_mesa.crear_jugador(id_jugador, nombre, edad)
        torneo_tenis_de_mesa.agregar_jugador(categoria, jugador, jugadores_por_categoria)
        print(f"Jugador registrado en la categoría {categoria} exitosamente.")
    elif (opcion == "2"):
        id_jugador1 = int(input("Ingrese el ID del primer jugador: "))
        id_jugador2 = int(input("Ingrese el ID del segundo jugador: "))
        sets_ganados_jugador1 = int(input("Ingrese los sets ganados por el primer jugador: "))
        sets_ganados_jugador2 = int(input("Ingrese los sets ganados por el segundo jugador: "))

        jugador1 = next((j for j in jugadores_por_categoria.values() for p in j if p['id'] == id_jugador1), None)
        jugador2 = next((j for j in jugadores_por_categoria.values() for p in j if p['id'] == id_jugador2), None)

        if jugador1 and jugador2:
            torneo_tenis_de_mesa.registrar_partido(jugador1, jugador2, sets_ganados_jugador1, sets_ganados_jugador2)
            print("Partido registrado exitosamente.")
        else:
            print("Al menos uno de los jugadores no ha sido registrado.")
    elif (opcion == "3"):
        categoria = input("Ingrese la categoría para obtener al ganador: ")
        print(torneo_tenis_de_mesa.obtener_ganador(categoria, jugadores_por_categoria))
    elif (opcion == "4"):
        break
    else:
        print("Opción no válida...")