cantidadDeCasos = int(input())
for _ in range(cantidadDeCasos):
    cantidadElementos, numeroObjetivo = map(int, input().split())
    conjuntoElementos = set(map(int, input().split()))
    esPrimiConjunto = True

    for divisor in range(1, int(numeroObjetivo ** 0.5) + 1):
        if numeroObjetivo % divisor == 0:
            if divisor not in conjuntoElementos:
                esPrimiConjunto = False
                break
            otroDivisor = numeroObjetivo // divisor
            if otroDivisor != divisor and otroDivisor not in conjuntoElementos:
                esPrimiConjunto = False
                break

    if esPrimiConjunto:
        print("Es PrimiConjunto")
    else:
        print("No es PrimiConjunto")


