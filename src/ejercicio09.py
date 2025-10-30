"""
Ejercicio 9: Simulador de Carrera de Caracoles

Descripción:
    Programa que simula una carrera entre 3 caracoles con velocidades diferentes.
    Cada caracol avanza según su velocidad en cada turno hasta que uno llegue a la meta.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def simular_carrera(velocidad1: int, velocidad2: int, velocidad3: int, distancia_meta: int) -> tuple[int, int]:
    if not (1 <= velocidad1 <= 10) or not (1 <= velocidad2 <= 10) or not (1 <= velocidad3 <= 10) or distancia_meta <= 0:
        return 0, 0

    distancia_v1 = distancia_v2 = distancia_v3 = 0
    turnos_necesarios = 0

    while max(distancia_v1, distancia_v2, distancia_v3) < distancia_meta:
        distancia_v1 += velocidad1
        distancia_v2 += velocidad2
        distancia_v3 += velocidad3
        turnos_necesarios += 1

    # Determinar el/los caracoles que alcanzaron la meta
    resultados = {
        1: distancia_v1,
        2: distancia_v2,
        3: distancia_v3
    }

    # Filtrar los que alcanzaron o superaron la meta
    ganadores = [num for num, dist in resultados.items() if dist >= distancia_meta]

    # En caso de empate, gana el caracol con número menor
    ganador = min(ganadores)

    return ganador, turnos_necesarios


def solicitar_velocidades() -> tuple[int, int, int]:
    """
    Solicita las velocidades de los 3 caracoles.
    
    Returns:
        tuple[int, int, int]: (velocidad1, velocidad2, velocidad3)
    """
    print("Introduce las velocidades de los caracoles (1-10 cm/turno):")
    
    velocidad1: int = 0
    while velocidad1 < 1 or velocidad1 > 10:
        entrada: str = input("Velocidad caracol 1: ")
        try:
            velocidad1 = int(entrada)
            if velocidad1 < 1 or velocidad1 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad1 = 0
    
    velocidad2: int = 0
    while velocidad2 < 1 or velocidad2 > 10:
        entrada: str = input("Velocidad caracol 2: ")
        try:
            velocidad2 = int(entrada)
            if velocidad2 < 1 or velocidad2 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad2 = 0
    
    velocidad3: int = 0
    while velocidad3 < 1 or velocidad3 > 10:
        entrada: str = input("Velocidad caracol 3: ")
        try:
            velocidad3 = int(entrada)
            if velocidad3 < 1 or velocidad3 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad3 = 0
    
    return (velocidad1, velocidad2, velocidad3)


def solicitar_distancia_meta() -> int:
    """
    Solicita la distancia de la meta.
    
    Returns:
        int: Distancia de la meta en cm (> 0)
    """
    distancia: int = 0
    
    while distancia <= 0:
        entrada: str = input("Distancia de la meta (cm): ")
        try:
            distancia = int(entrada)
            if distancia <= 0:
                print("Error: La distancia debe ser positiva")
        except ValueError:
            print("Error: Debe introducir un número entero")
            distancia = 0
    
    return distancia


def calcular_distancias_finales(vel1: int, vel2: int, vel3: int, turnos: int) -> tuple[int, int, int]:
    """
    Calcula las distancias alcanzadas por cada caracol.
    
    Args:
        vel1, vel2, vel3: Velocidades de los caracoles
        turnos: Número de turnos que duró la carrera
        
    Returns:
        tuple[int, int, int]: Distancias alcanzadas (dist1, dist2, dist3)
    """
    dist1: int = vel1 * turnos
    dist2: int = vel2 * turnos
    dist3: int = vel3 * turnos
    
    return (dist1, dist2, dist3)


def mostrar_resultado(ganador: int, turnos: int, vel1: int, vel2: int, vel3: int, distancia_meta: int) -> None:
    """
    Muestra el resultado de la carrera de forma visual.
    
    Args:
        ganador: Número del caracol ganador
        turnos: Número de turnos que duró la carrera
        vel1, vel2, vel3: Velocidades de los caracoles
        distancia_meta: Distancia de la meta
    """
    print("\n" + "=" * 50)
    print("🐌 RESULTADO DE LA CARRERA 🐌")
    print("=" * 50)
    
    print(f"\nDistancia de la meta: {distancia_meta} cm")
    print(f"Turnos necesarios: {turnos}")
    
    print("\nVelocidades:")
    print(f"  🐌 Caracol 1: {vel1} cm/turno")
    print(f"  🐌 Caracol 2: {vel2} cm/turno")
    print(f"  🐌 Caracol 3: {vel3} cm/turno")
    
    # Calcular distancias alcanzadas por cada caracol
    dist1: int
    dist2: int
    dist3: int
    dist1, dist2, dist3 = calcular_distancias_finales(vel1, vel2, vel3, turnos)
    
    print("\nDistancias alcanzadas:")
    print(f"  Caracol 1: {dist1} cm")
    print(f"  Caracol 2: {dist2} cm")
    print(f"  Caracol 3: {dist3} cm")
    
    print(f"\n🏆 ¡GANADOR: Caracol {ganador}!")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita las velocidades de los 3 caracoles (lectura)
        2. Solicita la distancia de la meta (lectura)
        3. Simula la carrera usando la función obligatoria (procesamiento)
        4. Muestra el resultado de forma visual (salida)
    """
    print("🐌 SIMULADOR DE CARRERA DE CARACOLES 🐌")
    print()
    
    # Paso 1: Lectura - Obtener velocidades
    vel1: int
    vel2: int
    vel3: int
    vel1, vel2, vel3 = solicitar_velocidades()
    
    # Paso 2: Lectura - Obtener distancia de la meta
    distancia: int = solicitar_distancia_meta()
    
    # Paso 3: Procesamiento - Simular carrera usando la función obligatoria
    ganador: int
    turnos: int
    ganador, turnos = simular_carrera(vel1, vel2, vel3, distancia)
    
    # Verificar si hubo error en la simulación
    if ganador == 0:
        print("\nError: Datos inválidos para la simulación")
        return
    
    # Paso 4: Salida - Mostrar resultado
    mostrar_resultado(ganador, turnos, vel1, vel2, vel3, distancia)


if __name__ == "__main__":
    main()
