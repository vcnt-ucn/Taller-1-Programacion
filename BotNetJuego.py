import random

SEPARADOR = "=" * 32
# para debug
DAÑO_DEBIL = 100
DAÑO_FUERTE = 20
DAÑO_CRITICO = 30

# loop principal
while True:
    # mostrar menu
    print("=" * 8 + " JUEGO - BOTNET " + "=" * 8)
    print("1. Comenzar")
    print("2. Salir")
    print(SEPARADOR)
    while True: # solicitar opcion
        try:
            opcion = int(input("Seleccione una opcion: "))
            break
        except ValueError:
            print("Error. Ingrese un numero valido.\n")
    match opcion:
        case 1: # comenzar
            seguridad = 100 # inicializar vida del admin
            partida_terminada = False
            # loop externo, nodos (3)
            for nodo in range(1, 4): # itera desde 1 hasta 4-1 (3)
                match nodo: # inicializar nivel de amenaza (vida del robot) segun el nodo actual
                    case 1:
                        nivel_amenaza = random.randint(100, 300) # al azar entre 100 y 300
                    case 2:
                        nivel_amenaza = random.randint(200, 400) # al azar entre 200 y 400
                    case 3:
                        nivel_amenaza = random.randint(300, 500) # al azar entre 300 y 500
                # inicio del combate
                print(f"\n>>> INICIANDO COMBATE CONTRA NODO {nodo}... <<<")
                print("NIVEL DE AMENAZA:", nivel_amenaza)
                turno = 1 # inicializar variable de turnos en 1
                nodo_neutralizado = False
                # loop interno, turnos
                while turno <= 10 and not nodo_neutralizado and seguridad > 0:
                    print(f"\n=== TURNO {turno}/10 - NODO {nodo}/3 ===")
                    numero_defensa = random.randint(1, 3) # al azar del 1 al 3
                    print("BOT ATACA. ADIVINA EL NUMERO (1, 2 o 3)")
                    while True: # solicitar opciones (1-3)
                        try:
                            respuesta_defensa = int(input("Tu respuesta: "))
                            if respuesta_defensa == 1 or respuesta_defensa == 2 or respuesta_defensa == 3: # si la opcion ingresada esta dentro de las 3 posibles devolver ese valor
                                break
                            print("Error. Ingrese un numero entre las opciones.") # si no, mostrar el error para volver a preguntar
                        except ValueError:
                            print("Error. Ingrese un numero valido.")
                    defensa_exitosa = (respuesta_defensa == numero_defensa) # guarda resultado, exitoso si la respuesta es igual al numero calculado previamente
                    if defensa_exitosa: # si la defensa fue exitosa, mostrar mensaje
                        print("\n>>> DEFENSA EXITOSA <<<")
                        print("NO SUFRES DAÑO")
                    else: # si no fue exitosa bajarle vida al admin
                        daño = random.randint(10, 20) # al azar del 10 al 20
                        seguridad -= daño # resta el daño a la vida del admin
                        print(f"\n>>> DEFENSA FALLIDA (Era {numero_defensa}) <<<")
                        print("HAS SUFRIDO", daño, "DE DAÑO")
                    if seguridad <= 0: # si el admin ya no tiene vida
                        seguridad = 0 # evita pasar a negativo
                        print("\n>>> LA SEGURIDAD LLEGO A 0 <<<")
                        print("HAS PERDIDO")
                        print(SEPARADOR, "\n\n")
                        partida_terminada = True
                        break # salir del loop
                    turno_gastado = False
                    # loop de acciones
                    while not turno_gastado and not nodo_neutralizado and seguridad > 0:
                        print("\n=== MENU DE ACCIONES ===")
                        print("1. Ataque Debil")
                        print("2. Ataque Fuerte")
                        print("3. Analizar Estado")
                        print(SEPARADOR)
                        while True: # solicitar opciones (1-3)
                            try:
                                accion = int(input("Tu respuesta: "))
                                if accion == 1 or accion == 2 or accion == 3: # si la opcion ingresada esta dentro de las 3 posibles devolver ese valor
                                    break
                                print("Error. Ingrese un numero entre las opciones.") # si no, mostrar el error para volver a preguntar
                            except ValueError:
                                print("Error. Ingrese un numero valido.")
                        match accion:
                            case 1: # ataque debil
                                nivel_amenaza -= DAÑO_DEBIL # bajarle vida al nodo
                                if nivel_amenaza < 0: # si el nodo ya no tiene vida
                                    nivel_amenaza = 0 # evita pasar a negativo
                                print("\n>>> ATAQUE DEBIL EJECUTADO <<<")
                                print("Amenaza baja a", nivel_amenaza)
                                turno_gastado = True
                            case 2: # ataque fuerte
                                numero_ataque = random.randint(1, 10) # al azar del 1 al 10
                                print("\n=== Adivina el numero (1-10): ===")
                                print("1. Mayor a 5")
                                print("2. Menor a 5")
                                print("3. Igual a 5")
                                print(SEPARADOR)
                                while True: # solicitar opciones (1-3)
                                    try:
                                        opcion = int(input("Tu respuesta: "))
                                        if opcion == 1 or opcion == 2 or opcion == 3: # si la opcion ingresada esta dentro de las 3 posibles devolver ese valor
                                            break
                                        print("Error. Ingrese un numero entre las opciones.") # si no, mostrar el error para volver a preguntar
                                    except ValueError:
                                        print("Error. Ingrese un numero valido.")
                                if (opcion == 1 and numero_ataque > 5) or (opcion == 2 and numero_ataque < 5): # si se escogio la opcion 1 o 2 y es correcta
                                    nivel_amenaza -= DAÑO_FUERTE # bajarle vida al nodo con doble ataque
                                    if nivel_amenaza < 0: # si el nodo ya no tiene vida
                                        nivel_amenaza = 0 # evita pasar a negativo
                                    print(f"\n>>> ¡ACERTASTE (Era {numero_ataque})! <<<")
                                    print("Amenaza baja a", nivel_amenaza)
                                elif opcion == 3 and numero_ataque == 5: # si se escogio la opcion 3 y es correcta
                                    nivel_amenaza -= DAÑO_CRITICO # bajarle vida al nodo con triple ataque
                                    if nivel_amenaza < 0: # si el nodo ya no tiene vida
                                        nivel_amenaza = 0 # evita pasar a negativo
                                    print("\n>>> ¡CRÍTICO! <<<")
                                    print("Amenaza baja a", nivel_amenaza)
                                else: # si se escogio cualquier opcion y no es correcta
                                    print(f"\n>>> FALLASTE (Era {numero_ataque}) <<<")
                                    print("No se ejerce daño")
                                turno_gastado = True
                            case 3: # analizar estado, no gasta turno
                                print("\n=== ESTADO ===")
                                print("Turno Actual:", turno)
                                print("Nivel de Seguridad Actual:", seguridad)
                                print("Nivel de Amenaza Actual:", nivel_amenaza)
                                print(SEPARADOR)
                    if nivel_amenaza <= 0: # si el nodo ya no tiene vida
                        nivel_amenaza = 0 # evita pasar a negativo
                        nodo_neutralizado = True
                        print("\n>>> NODO", nodo, "NEUTRALIZADO <<<")
                        nodos_restantes = 3 - nodo # calcular nodos restantes, total - actual
                        if nodos_restantes > 0: # mostrar nodos restantes
                            print("NODOS RESTANTES:", nodos_restantes)
                        break # terminar loop interno
                    turno += 1 # sumar uno a la variable para avanzar al siguiente turno
                # termino del turno analizar estado de la partida
                if nodo_neutralizado: # verifica si hemos eliminado el nodo para pasar al siguiente
                    if nodos_restantes > 0: # si aun quedan nodos
                        print("\nAVANZANDO AL SIGUIENTE NODO...")
                elif not partida_terminada:
                    print("\n>>> FIN DE LOS TURNOS <<<")
                    if nodo == 3: # sistema de mecanismo de emergencia solo para el nodo 3
                        print("EVALUANDO MECANISMO DE EMERGENCIA...")
                        if nivel_amenaza <= 50: # solo se activa con un 30% de exito si la vida del nodo es menor o igual a 50
                            print("\nNIVEL DE AMENAZA MENOR A 50")
                            print("ACTIVANDO PROTOCOLO (30% de éxito)...")
                            probabilidad = random.randint(1, 10) # al azar del 1 al 10 (10% al 100%)
                            if probabilidad <= 3: # si es menor o igual a 3 (30% de probabilidad)
                                nivel_amenaza = 0 # elimina al nodo inmediatamente
                                print("\n>>> EXITOSO <<<")
                                print("AMENAZA HA BAJADO A 0")
                                print("HAS GANADO")
                                print(SEPARADOR, "\n\n")
                                partida_terminada = True
                            else:
                                print("\n>>> FALLIDO <<<")
                                print("HAS PERDIDO")
                                print(SEPARADOR, "\n\n")
                                partida_terminada = True
                        else:
                            print("\n>>> NO SE HA ACTIVADO EL MECANISMO DE EMERGENCIA <<<")
                            print("NIVEL DE AMENAZA MAYOR A 50")
                            print("HAS PERDIDO")
                            print(SEPARADOR, "\n\n")
                            partida_terminada = True
                    else:
                        print("NO SE NEUTRALIZO EL NODO")
                        print("HAS PERDIDO")
                        print(SEPARADOR, "\n\n")
                        partida_terminada = True
                if partida_terminada:
                    break # salir del loop de nodos
            # si el admin aun tiene vida al terminar el loop externo, mostrar mensaje de victoria
            if not partida_terminada and seguridad > 0:
                print("\n=== VICTORIA TOTAL ===")
                print("HAS NEUTRALIZADO A TODOS LOS NODOS")
                print("SEGURIDAD FINAL:", seguridad)
                print(SEPARADOR, "\n\n")
        case 2: # salir
            print("\nSaliendo...")
            break # apagar el programa
        case _:
            print("\nOpcion invalida. Intentalo de nuevo.")
