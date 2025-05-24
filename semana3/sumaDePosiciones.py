def leerEnteros():
    return list(map(int, input().split()))

def sumarPosiciones(arreglo, consultas):
    posiciones = {}
    for i in range(len(arreglo)):
        posiciones[arreglo[i]] = i + 1
    total = 0
    for x in consultas:
        if x in posiciones:
            total += posiciones[x]
    return total

def sumaPosiciones():
    n = int(input())
    arreglo = leerEnteros()
    m = int(input())
    consultas = leerEnteros()
    print(sumarPosiciones(arreglo, consultas))

sumaPosiciones()
