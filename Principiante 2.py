"""
PROGRAMA PARA CALCULAR EL IMC...
"""
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese edad del estudiante: ")

def calcular_imc(peso, altura):
    return peso /(altura ** 2)

def clasificar_imc(imc):
    if (imc <= 24.9):
        return "Normal"
    elif (25 >= imc >= 29.9):
        return "Sobrepeso"
    elif (30 >= imc >= 34.9):
        return "Obesidad I"
    elif (35 >= imc >= 39.9):
        return "Obesidad II"
    else:
        return "Obesidad III"
    
peso = float(input("Ingrese el peso del estudiante en kilogramos (Kg): "))
altura = float(input("Ingrese la altura del estudiante en metros: "))

imc = calcular_imc(peso, altura)
categoria_imc = clasificar_imc(imc)

print("Informacion del estudiante: ")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"IMC: {imc}")
print(f"Categoria IMC: {categoria_imc}")