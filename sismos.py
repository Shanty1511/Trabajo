"""
++++++++++++++++++++++++
+ PREVENCION DE SISMOS +
++++++++++++++++++++++++
"""
def registrar_ciudad(ciudades, nombre_ciudad, num_sismos):
    ciudades.append({
        'nombre': nombre_ciudad,
        'sismos': [0] * num_sismos
    })
def registrar_sismo(ciudades, nombre_ciudad, num_sismo, magnitud):
    for ciudad in ciudades:
        if ciudad['nombre'] == nombre_ciudad:
            ciudad['sismos'][num_sismo - 1] = magnitud
            break

def buscar_sismos(ciudades, nombre_ciudad):
    for ciudad in ciudades:
        if ciudad['nombre'] == nombre_ciudad:
            return ciudad['sismos']
    return None

def informe_riesgo(ciudades):
    riesgos = []
    for ciudad in ciudades:
        promedio_sismos = sum(ciudad['sismos']) / len(ciudad['sismos'])
        if promedio_sismos < 2.5:
            riesgos.append("Amarillo (Sin riesgo)")
        elif 2.6 <= promedio_sismos <= 4.5:
            riesgos.append("Naranja (Riesgo medio)")
        else:
            riesgos.append("Rojo (Riesgo alto)")
    return riesgos
