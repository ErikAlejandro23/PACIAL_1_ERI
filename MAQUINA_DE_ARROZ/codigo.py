
# Creamos una lista vacía que representa la caja de distribución.
caja = []

# Inicializamos el contador de bolsas empacadas.
contador = 0

# Mostramos el nombre y el estado inicial de la máquina.
print("=== MÁQUINA EMPACADORA DE ARROZ ===")
print("Sistema iniciado.")

# Mantenemos la máquina funcionando hasta que el operador la detenga.
while True:

    # Solicitamos información sobre la disponibilidad de una bolsa.
    respuesta = input(
        "\n¿Hay una bolsa disponible? (s/n) "
        "o escribe q para detener: "
    ).strip().lower()

    # Si el operador escribe q, finalizamos la simulación.
    if respuesta == "q":
        print("Deteniendo la máquina de forma controlada...")
        break

    # Si no hay bolsa, no iniciamos el llenado.
    elif respuesta == "n":
        print("No hay bolsa disponible.")
        print("Esperando una bolsa para continuar...")
        continue

    # Si la respuesta no es s, n o q, la entrada es inválida.
    elif respuesta != "s":
        print("Respuesta inválida. Escribe s, n o q.")
        continue

    # Registramos una bolsa nueva mediante un diccionario.
    bolsa = {
        "numero": contador + 1,
        "llena": False,
        "sellada": False
    }

    # Paso 1: confirmamos que existe una bolsa disponible.
    print("Paso 1: Bolsa detectada correctamente.")

    # Paso 2: simulamos el llenado con arroz.
    bolsa["llena"] = True
    print("Paso 2: Bolsa llenada con arroz.")

    # Paso 3: sellamos la bolsa solamente después de llenarla.
    if bolsa["llena"]:
        bolsa["sellada"] = True
        print("Paso 3: Bolsa sellada correctamente.")

    # Paso 4: empacamos solamente una bolsa llena y sellada.
    if bolsa["llena"] and bolsa["sellada"]:

        # Agregamos la bolsa terminada a la lista de la caja.
        caja.append(bolsa)

        # Actualizamos el número de bolsas empacadas.
        contador += 1

        print(f"Paso 4: Bolsa {contador} colocada en la caja.")
        print("Proceso completado correctamente.")

# Mostramos el resumen cuando se detiene la simulación.
print("\n=== RESUMEN DE PRODUCCIÓN ===")
print(f"Total de bolsas empacadas: {contador}")

# Mostramos las bolsas almacenadas en la caja.
print("Contenido de la caja:")

for bolsa in caja:
    print(
        f"Bolsa {bolsa['numero']}: "
        f"Llena = {bolsa['llena']}, "
        f"Sellada = {bolsa['sellada']}"
    )

print("Simulación finalizada.")
