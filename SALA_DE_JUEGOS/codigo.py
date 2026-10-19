
# Mostramos el título del programa.
print("=== SALA DE JUEGOS DIVERSIÓN TOTAL ===")

# Solicitamos la edad del cliente.
entrada = input("Ingrese la edad del cliente: ")

# Comprobamos que la entrada contenga solamente dígitos.
if entrada.isdigit():

    # Convertimos la edad a un número entero.
    edad = int(entrada)

    # Verificamos que el cliente tenga una edad válida.
    if edad >= 0:

        # Los menores de 5 años entran gratis.
        if edad < 5:
            precio = 0

        # Desde los 5 hasta los 18 años pagan 5.
        elif edad <= 18:
            precio = 5

        # Los mayores de 18 años pagan 10.
        else:
            precio = 10

        # Mostramos la edad y el precio de entrada.
        print(f"Edad del cliente: {edad} años")
        print(f"Precio de la entrada: ${precio}")

        # Mostramos un mensaje según la tarifa.
        if precio == 0:
            print("¡La diversión es gratis para ti!")
        else:
            print("¡Gracias por visitar nuestra sala de juegos!")

    else:
        # Mensaje para una edad negativa.
        print("Error: la edad no puede ser negativa.")

else:
    # Mensaje cuando la entrada no es un número entero.
    print("Error: ingresa la edad usando un número entero.")
