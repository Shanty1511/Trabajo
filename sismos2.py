"""
++++++++++++++++++++++++
+ PREVENCION DE SISMOS +
++++++++++++++++++++++++
"""
import os
import sismos

cantidadMaxima = 5
ciudadesRegistradas = 0

isActive = True
opMenu = 0
menu = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar Sismo por ciudad\n4. Informe de riesgo\n5. Salir\n:)"

def main():
    global isActive, ciudadesRegistradas

    ciudades = []
    while isActive:
        os.system("cls")
        try:
            opMenu = int(input(menu))
        except ValueError:
            print("Error en el dato de ingreso...")
            input("Presione Enter para continuar...")
            continue 
        if (opMenu == 1):
            if ciudadesRegistradas < cantidadMaxima:
                nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
                num_sismos = int(input("Ingrese la cantidad de sismos a registrar para esta ciudad: "))
                sismos.registrar_ciudad(ciudades, nombre_ciudad, num_sismos)
                ciudadesRegistradas += 1
            else:
                print("Has alcanzado el tope de ciudades registradas...")
                input("Presione Enter para continuar...")
        elif (opMenu == 2):
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            num_sismo = int(input("Ingrese el número del sismo a registrar: "))
            magnitud = float(input("Ingrese la magnitud del sismo: "))
            sismos.registrar_sismo(ciudades, nombre_ciudad, num_sismo, magnitud)
        elif (opMenu == 3):
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            sismos_ciudad = sismos.buscar_sismos(ciudades, nombre_ciudad)
            if sismos_ciudad:
                print(f"Sismos en {nombre_ciudad}: {sismos_ciudad}")
            else:
                print(f"No se encontraron sismos para {nombre_ciudad}")
        elif (opMenu == 4):
            riesgos = sismos.informe_riesgo(ciudades)
            for i, ciudad in enumerate(ciudades):
                print(f"Riesgo en {ciudad['nombre']}: {riesgos[i]}")
        elif (opMenu == 5):
            isActive = False
        else:
            print("Opción no válida...")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()