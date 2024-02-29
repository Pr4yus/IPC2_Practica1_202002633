class Producto:
    def __init__(self, nombre, codigo, precio, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.descripcion = descripcion
        

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

class Compra:
    def __init__(self, cliente, id_compra):
        self.cliente = cliente
        self.id_compra = id_compra
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def generar_factura(self):
        costo_total = 0
        for producto in self.lista_productos:
            costo_total += producto.precio
        impuesto = costo_total * 0.12
        return costo_total, impuesto
    
productos = []
clientes = []
compras = []

def menu_principal():
    print("=== Bienvenido al Sistema de Gestión ===")
    print("1. Registrar Nuevo Producto")
    print("2. Registrar Nuevo Cliente")
    print("3. Realizar Compra")
    print("4. Generar Reporte de Compra")
    print("5. Información del Estudiante")
    print("6. Salir")

def registrar_producto():
    print("----- Registro de Producto -----")
    nombre = input("Ingrese el nombre del producto: ")
    codigo = input("Ingrese el código del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    return Producto(nombre, codigo, precio, descripcion)

def registrar_cliente():
    print("----- Registro de Cliente -----")
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")
    return Cliente(nombre, correo, nit)

def realizar_compra(clientes, productos):
    print("----- Realizar Compra -----")
    nit = input("Ingrese el NIT del cliente: ")
    cliente_actual = None
    for cliente in clientes:
        if cliente.nit == nit:
            cliente_actual = cliente
            break
    if cliente_actual:
        id_compra = len(compras) + 1
        compra_actual = Compra(cliente_actual, id_compra)
        while True:
            print("------------- Menú Compra -------------")
            print("1. Agregar Producto al Carrito")
            print("2. Finalizar Compra y Generar Factura")
            print("--------------------------------------")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                codigo_producto = input("Ingrese el código del producto: ")
                producto_encontrado = None
                for producto in productos:
                    if producto.codigo == codigo_producto:
                        producto_encontrado = producto
                        break
                if producto_encontrado:
                    compra_actual.agregar_producto(producto_encontrado)
                else:
                    print("Producto no encontrado")
            elif opcion == "2":
                costo_total, impuesto = compra_actual.generar_factura()
                print(f"Total: Q{costo_total:.2f}")
                print(f"Impuesto: Q{impuesto:.2f}")
                compras.append(compra_actual)
                print("Compra finalizada correctamente.")
                break
            else:
                print("Opción no válida")
    else:
        print("El cliente no está registrado")

def reporte_compra():
    print("----- Reporte de Compra -----")
    id_compra = int(input("Ingrese el ID de la compra: "))
    compra_encontrada = None
    for compra in compras:
        if compra.id_compra == id_compra:
            compra_encontrada = compra
            break
    if compra_encontrada:
        print("------------- REPORTE DE COMPRA -------------")
        print("Cliente:")
        print("Nombre:", compra_encontrada.cliente.nombre)
        print("Correo electrónico:", compra_encontrada.cliente.correo)
        print("NIT:", compra_encontrada.cliente.nit)
        print("PRODUCTOS COMPRADOS:")
        for i, producto in enumerate(compra_encontrada.lista_productos, 1):
            print(f"{i}. {producto.nombre}: Q{producto.precio:.2f}")
        costo_total, impuesto = compra_encontrada.generar_factura()
        print(f"Total: Q{costo_total:.2f}")
        print(f"Impuestos: Q{impuesto:.2f}")
        print("------------------------------------------")
    else:
        print("Compra no encontrada")

def informacion_estudiante():
    print("Nombre del estudiante: Abner Palacios")
    print("Número de carnet: 202002633")



while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        producto = registrar_producto()
        productos.append(producto)
        print("Producto registrado exitosamente")
    elif opcion == "2":
        cliente = registrar_cliente()
        clientes.append(cliente)
        print("Cliente registrado exitosamente")
    elif opcion == "3":
        realizar_compra(clientes, productos)
    elif opcion == "4":
        reporte_compra()
    elif opcion == "5":
        informacion_estudiante()
    elif opcion == "6":
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opción inválida, ingrese una opcion válida")
