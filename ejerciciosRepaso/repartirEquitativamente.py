def main():
    # Leer los valores de M (niños) y N (dulces)
    entrada = input().split()
    M = int(entrada[0])
    N = int(entrada[1])

    # Leer los valores de los dulces (sabores)
    sabores = list(map(int, input().split()))

    # Crear lista para acumular el sabor total por niño
    acumulado = [0] * M

    # Crear lista para guardar los dulces que recibe cada niño
    recibidos = [[] for _ in range(M)]

    # Repartir los dulces uno por uno, usando i % M
    for i in range(N):
        nino = i % M  # Esto da el índice del niño
        acumulado[nino] += sabores[i]  # Sumar el sabor del dulce
        recibidos[nino].append(sabores[i])  # Guardar el dulce recibido

    # Mostrar los dulces recibidos por cada niño
    for i in range(M):
        print(f"Niño {i} recibió: {recibidos[i]} (Total: {sum(recibidos[i])})")

    # Buscar el índice del niño con mayor sabor total
    mayor_valor = acumulado[0]
    indice_mayor = 0
    for i in range(1, M):
        if acumulado[i] > mayor_valor:
            mayor_valor = acumulado[i]
            indice_mayor = i

    # Imprimir el índice del niño con más sabor
    print(indice_mayor)


if __name__ == "__main__":
    main()

    