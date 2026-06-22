#Juego Piedra Papel Tijera
import random

# Para inicializar las variables
Pts_us = 0
Pts_pc = 0
Cont_juego = 1

#Incio del primer bucle
while Cont_juego == 1:
    # Le damos a conocer las opciones al usuario
    print("Elige tu opción: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    op_us = int(input("Ingresa el número de tu opción: "))

    # Para que la computadora elija su opción
    op_pc = random.randint(1, 3)

    # Mostrar las opciones elegidas
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    print(f"Elegiste la opcion: {opciones[op_us]}")
    print(f"Opción de la computadora: {opciones[op_pc]}")

    # Usamos un IF para determinar el resultado del juego
    if op_us == op_pc:
        print("Han empatado!!")
    # En caso contrario de que el primer if no se cumpla, se evalua si el usuario gana con este segundo if anidido    
    elif (op_us == 1 and op_pc == 3) or (op_us == 2 and op_pc == 1) or (op_us == 3 and op_pc == 2):
        print("Ganaste la ronda!!")
        Pts_us += 1
    # Y para finalizar utilizamos else para que en caso de que no ocurra ninguna opcion anterior, el usuario pierda
    else:
        print("Haz perdido esta ronda :(")
        Pts_pc += 1
    # Mostrar el resultado final
    print(f"Tu puntuación: {Pts_us}")
    print(f"Puntuación de la computadora: {Pts_pc}")
    # Preguntar si quiere jugar otra vez
    Cont_juego= input("¿Quieres jugar otra vez? (1=Si / 0=No): ")
print("Gracias por jugar :3")