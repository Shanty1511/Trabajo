"""
PROGRAMA PARA LEER TRES NUMEROS POSITIVOS Y SUMARLOS...
"""
def leer_entero_positivo():
    while True:
        try:
            numero = int(input("Ingrese numero positivo por favor..."))
            if numero > 0:
                return numero
            else:
                print("Ingrese numero positivo por favor... ")
        except ValueError:
            print("Valor ingresado incorrecto...")

numero1 = leer_entero_positivo()
numero2 = leer_entero_positivo()
numero3 = leer_entero_positivo()

suma = numero1 + numero2 + numero3

print(f"La suma de los tres números es: {suma}")