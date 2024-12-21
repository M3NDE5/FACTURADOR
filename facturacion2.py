# "pr" significa productos
# "cl" significa clientes
# "fc" significa facturas


def crear_producto(pr):
    print("\n||||| CREAR PRODUCTO |||||")
    x = int(input("Ingrese el numero de productos: "))
    for i in range(x):
        producto = str(input("Ingrese el producto: "))
        cod = str(input("Ingrese el codigo: "))
        valor = int(input("Ingrese el valor: "))
        pr[(producto, cod)] = valor


def crear_cliente(cl):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cedula_cliente = input("Ingrese la cedula del cliente: ")
    telefono_cliente = input("Ingrese la cedula del cliente: ")
    cl['nombre'] = nombre_cliente
    cl['cedula'] = cedula_cliente
    cl['telefono'] = telefono_cliente

def crear_factura(pr, cl, fc):
    factura={
        'cliente' : cl.copy(),
        'productos': pr.copy(),
    }
    print("\n----- FACTURA -----")
    print(f"Cliente: {factura['cliente']['nombre']}")
    print(f"Cedula: {factura['cliente']['cedula']}")
    print(f"Telefono: {factura['cliente']['telefono']}")
    print("Productos:")
    for (producto, codigo), valor in factura["productos"].items():
        print(f"|| producto: {producto} || codigo: {codigo} || valor: {valor} ||")
    suma = 0
    for (producto, codigo), valor in factura["productos"].items():
        suma += valor
    print(f"Total a pagar: {suma}")

    fc.append(factura)


def almacenar_facturas(fc):
    contador = 0
    print("\nFACTURAS ALMACENADAS")
    for factura in fc:
        print(f"\nFACTURA {contador + 1}")
        print(f"CLIENTE: {factura["cliente"]}")
        print(f"PRODUCTOS: {factura["productos"]}")
        contador += 1

def buscar_facturas(fc):
    nombre_buscar = str(input("Ingresa el nombre del cliente a buscar: "))
    for factura in fc:
        if factura['cliente']['nombre'] == nombre_buscar:
            print("Factura encontrada.....")
            print("\n----- FACTURA -----")
            print(f"Cliente: {factura['cliente']['nombre']}")
            print(f"Cedula: {factura['cliente']['cedula']}")
            print(f"Telefono: {factura['cliente']['telefono']}")
            for (producto, codigo), valor in factura["productos"].items():
                print(f"|| producto: {producto} || codigo: {codigo} || valor: {valor} ||")
            suma = 0
            for (producto, codigo), valor in factura["productos"].items():
                suma += valor
            print(f"Total a pagar: {suma}")
        else:
            print("El producto no ha sido encontrado...")
        
        



productos = {}
clientes = {}
facturas = []
opc = 0
while opc!= 6:
    print("\nMENU FACTURACION \n1. Crear producto\n2. Crear cliente\n3. Mostrar factura\n4. Facturas registradas\n5. Buscar facturas")
    opc = int(input("\nIngrese una opcion: "))
    match opc:
        case 1:
            crear_producto(productos)
        case 2:
            crear_cliente(clientes)
        case 3:
            crear_factura(productos, clientes, facturas)
            productos.clear()
            clientes.clear()
        case 4:
            almacenar_facturas(facturas)
        case 5:
            buscar_facturas(facturas)

            
        
            

