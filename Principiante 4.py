"""
PROGRAMA QUE INGRESA NUMEROS POSITIVOS Y PARA CUANDO ENTRA UN NUMERO NEGATIVO...
"""
totalnumeros = 0
totalpares = 0
cantidadimpares = 0
sumaimpares = 0
sumapares = 0
menores10 = 0
entre20y50 = 0
mayores100 = 0
while True:
    numero = int(input("Ingrese un número positivo (Numero negativo para terminar el programa): "))
    if numero < 0:
        break
    totalnumeros += 1
    if numero % 2 == 0:
        totalpares += 1
        sumapares += numero
    else:  
        cantidadimpares += 1
        sumaimpares += numero
    if numero < 10:
        menores10 += 1
    elif 20 <= numero <= 50:
        entre20y50 += 1
    elif numero > 100:
        mayores100 += 1

promedio_pares = sumapares / totalpares if totalpares > 0 else 0
promedio_impares = sumaimpares / cantidadimpares if cantidadimpares > 0 else 0

print("Reporte:")
print(f"a.Total de numeros ingresados: {totalnumeros}")
print(f"b.Total numeros pares ingresados: {totalpares}")
print(f"c.Promedio de los numeros pares: {promedio_pares:.2f}")
print(f"d.Promedio de los numeros impares: {promedio_impares:.2f}")
print(f"e.Cuantos numeros son menores que 10: {menores10}")
print(f"f.Cuantos nuemros estan entre 20 y 50: {entre20y50}")
print(f"g.Cuantos numeros son mayores que 100: {mayores100}")