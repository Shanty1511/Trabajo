"""
PROGRAMA PARA CALCULAR EL IMC...
"""
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
    
peso_ideal_count = 0
sobre_peso_count = 0
obesidad_I_count = 0
obesidad_II_count = 0
obesidad_III_count = 0 
    
for _ in range(20):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese edad del estudiante: ")
    peso = float(input("Ingrese el peso del estudiante en kilogramos (Kg): "))
    altura = float(input("Ingrese la altura del estudiante en metros: "))

    imc = calcular_imc(peso, altura)
    categoria_imc = clasificar_imc(imc)
    
    if categoria_imc == "Normal":
        peso_ideal_count += 1
    elif categoria_imc == "Sobrepeso":
        sobre_peso_count += 1
    elif categoria_imc == "Obesidad I":
        obesidad_I_count += 1
    elif categoria_imc == "Obesidad II":
        obesidad_II_count += 1
    elif categoria_imc == "Obesidad III":
        obesidad_III_count += 1

    print("Informacion del estudiante: ")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"IMC: {imc:.2f}")
    print(f"Categoria IMC: {categoria_imc}")

print("Registro del estado de salud de la comunidad estudiantil")
print(f"a. Estudaintes en el peso ideal: {peso_ideal_count}")
print(f"b. Estudiantes en Obesidad I: {obesidad_I_count}")
print(f"c.Estudiantes en Obesidad II: {obesidad_II_count}")
print(f"d.Estudiantes en Obesidad III: {obesidad_III_count}")
print(f"e.Estudiantes en sobrepeso: {sobre_peso_count}")