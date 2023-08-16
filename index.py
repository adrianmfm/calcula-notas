def calcular_promedio(notas):
    total_notas = len(notas)
    suma_notas = sum(notas)
    promedio_notas = suma_notas / total_notas
    return promedio_notas


def main():
    notas = []
    try:
        cantidad_notas = int(input("¿Cuántas notas deseas calcular?: "))
        for i in range(cantidad_notas):
            nota = float(input(f"Ingresa la nota {i+1} (0 para salir): "))
            if nota == 0:
                break
            notas.append(nota)
    except ValueError:
        print("Debe ingresar un valor numérico válido.")

    if len(notas) > 0:
        promedio = calcular_promedio(notas)
        print("El promedio de las notas es:", promedio)
    else:
        print("No se ingresaron notas.")

if __name__ == "__main__":
    main()