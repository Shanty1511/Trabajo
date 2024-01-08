def crear_jugador(id_jugador, nombre, edad):
    return {
        'id': id_jugador,
        'nombre': nombre,
        'edad': edad,
        'partidos_jugados': 0,
        'partidos_ganados': 0,
        'partidos_perdidos': 0,
        'puntos_a_favor': 0,
        'puntos_en_contra': 0,
        'total_puntos': 0
    }

def agregar_jugador(categoria, jugador, jugadores_por_categoria):
    if categoria not in jugadores_por_categoria:
        jugadores_por_categoria[categoria] = []
    jugadores_por_categoria[categoria].append(jugador)

def iniciar_torneo(categoria, jugadores_por_categoria):
    if categoria in jugadores_por_categoria and len(jugadores_por_categoria[categoria]) >= 5:
        return True
    else:
        return False

def registrar_partido(jugador1, jugador2, sets_ganados_jugador1, sets_ganados_jugador2):
    jugador1['partidos_jugados'] += 1
    jugador2['partidos_jugados'] += 1

    if sets_ganados_jugador1 > sets_ganados_jugador2:
        jugador1['partidos_ganados'] += 1
        jugador1['puntos_a_favor'] += sets_ganados_jugador1 - sets_ganados_jugador2
        jugador2['puntos_en_contra'] += sets_ganados_jugador1 - sets_ganados_jugador2
    else:
        jugador2['partidos_ganados'] += 1
        jugador2['puntos_a_favor'] += sets_ganados_jugador2 - sets_ganados_jugador1
        jugador1['puntos_en_contra'] += sets_ganados_jugador2 - sets_ganados_jugador1

    jugador1['total_puntos'] = jugador1['partidos_ganados'] * 2 + jugador1['puntos_a_favor']
    jugador2['total_puntos'] = jugador2['partidos_ganados'] * 2 + jugador2['puntos_a_favor']

def obtener_ganador(categoria, jugadores_por_categoria):
    if categoria in jugadores_por_categoria:
        jugadores = jugadores_por_categoria[categoria]
        jugadores.sort(key=lambda x: (x['total_puntos'], x['puntos_a_favor']), reverse=True)

        if len(jugadores) > 0:
            ganador = jugadores[0]
            return f"Ganador en la categoría {categoria}: {ganador['nombre']} (ID: {ganador['id']})"
        else:
            return f"No hay jugadores registrados en la categoría {categoria}"
    else:
        return f"No existe la categoría {categoria}"