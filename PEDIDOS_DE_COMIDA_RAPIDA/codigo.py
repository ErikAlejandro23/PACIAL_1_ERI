

# Creamos un diccionario con los productos y sus precios.
menu = {
    1: ("Hamburguesa", 12000),
    2: ("Perro caliente", 9000),
    3: ("Pizza personal", 14000),
    4: ("Salchipapa", 20000),
    5: ("Patacon", 14000)
}

# Creamos una lista para almacenar los pedidos.
pedidos = []

# Mostramos el nombre del restaurante.
print("===================================")
print("           EL BUEN SABOR           ")
print("===================================")

# Mostramos los productos disponibles.
print("\nMENÚ:")
for numero, producto in menu.items():
    nombre, precio = producto
    print(f"{numero}. {nombre} - ${precio:,}")

# Permitimos registrar varios pedidos.
while True:

    # Solicitamos un producto válido.
    while True:
        opcion = input(
            "\nElige un producto (1-5) o escribe 0 para terminar: "
        ).strip()

        # Verificamos si el usuario quiere terminar.
        if opcion == "0":
            break

        # Verificamos que la opción exista en el menú.
        if opcion.isdigit() and int(opcion) in menu:
            opcion = int(opcion)

            # Separamos el nombre y el precio del producto.
            nombre_producto, precio = menu[opcion]

            # Guardamos el pedido.
            pedido = {
                "producto": nombre_producto,
                "precio": precio
            }

            pedidos.append(pedido)

            # Confirmamos el pedido.
            print(
                f"¡LLA ROMPISTE PAPU! Agregamos "
                f"{nombre_producto} por ${precio:,}."
            )

            break

        else:
            print(
                "No mi rey no hay! pide algo que te guste, no seas mamón. "
                "Por favor, vuelve a intentarlo."
            )

    # Si escribió 0, terminamos de recibir pedidos.
    if opcion == "0":
        break

# Mostramos el resumen de compra.
print("\n========== RESUMEN DE COMPRA ==========")

total = 0

for pedido in pedidos:
    print(
        f"{pedido['producto']} - ${pedido['precio']:,}"
    )

    total += pedido["precio"]

print("---------------------------------------")
print(f"TOTAL A PAGAR: ${total:,}")
print("¡Gracias por elegir El Buen Sabor!")
print("¡Que tengas un excelente día!")
