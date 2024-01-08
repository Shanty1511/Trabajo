"""
GESTION DE INVENTARIO
"""
class Producto:
    def __init__(self,codigo,nombre,valorCompra, valorVenta, stockMinimo,stockMaximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valorCompra = valorCompra
        self.valorVenta = valorVenta
        self.stockMaximo = stockMaximo
        self.stockMinimo = stockMinimo
        self.proveedor = proveedor
        self.stockActual = 0

def registrarProducto(inventario, codigo, nombre, valorCompra, valorVenta, stockMinimo, stockMaximo, proveedor):
    producto = Producto(codigo, nombre, valorCompra, valorVenta, stockMinimo, stockMaximo, proveedor)
    inventario[codigo] = producto
    print(f"Producto {nombre} registrado exitosamente...")

def verProductos(inventario):
    print("Lista de productos:")
    for producto in inventario.values():
        print(f"Codigo: {producto.codigo}, Nombre: {producto.nombre}, Valor de compra: {producto.valorCompra}, Valor de venta: {producto.valorVenta}, Stock actual: {producto.stockActual}, Stock minimo: {producto.stockMinimo}, Stock maximo: {producto.stockMaximo}, Proveedor: {producto.proveedor}")

def actualizarStock (inventario, codigo, cantidad):
    for producto in inventario:
        if producto.codigo == codigo:
            producto.stockActual += cantidad
            print (f"Actualizacion de stock en el producto {producto.nombre}\n Nuevo stock: {producto.stockActual}")
            break
    else:
        print(f"No se encontro el producto con el codigo {codigo}...")

def informeProductosCriticos (inventario):
    print("Productos criticos: ")
    for producto in inventario:
        if producto.stockActual < producto.stockMinimo:
            print(f"Codigo: {producto.codigo}, Nombre: {producto.nombre}\n Stock actual: {producto.stockActual}\n Stock minimo: {producto.stockMinimo}")

def gananciaPotencial (inventario):
    gananciaTotal = 0
    for producto in inventario:
        gananciaTotal += (producto.valorVenta - producto.valorCompra)* producto.stockActual
    return gananciaTotal

def main():
    inventario = {}

    while True:
        print("1. Registrar Producto\n 2.Visualizar Producto\n 3. Actualizar Stock\n 4. Informe de producto criticos\n 5. Calculo de ganancia potencial\n 6. Salir")
        opcion = input("Seleccione una opcion...")
        if opcion == '1':
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            valorVenta = float(input("Ingrese el valor de venta del producto: "))
            valorCompra = float(input("Ingrese el valor de compra del producto: "))
            stockMinimo = int(input("Ingrese el stock minimo del producto: "))
            stockMaximo = int(input("Ingrese el stock maximo del producto: "))
            proveedor = input("Ingrese el proveedor del producto: ")
            registrarProducto(inventario, codigo, nombre, valorCompra, valorVenta, stockMaximo, stockMinimo, proveedor)
        elif (opcion == 2):
            verProductos(inventario)
        elif (opcion == 3):
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad de stock a sumar o restar: "))
            actualizarStock(inventario, codigo, cantidad)
        elif (opcion == 4):
            informeProductosCriticos(inventario)
        elif (opcion == 5):
            ganancia_potencial = gananciaPotencial(inventario)
            print(f"Ganancia Potencial Total: {ganancia_potencial}")
        elif (opcion == 6):
            break
        else:
            print("Opción no válida...")

if __name__ == "__main__":
    main()