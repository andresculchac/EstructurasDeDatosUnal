#Hecho con AI

from bisect import bisect_left, insort

def contarInversiones(arr):
    listaOrdenada = []
    inversiones = 0
    for num in arr:
        pos = bisect_left(listaOrdenada, num)
        # Elementos mayores ya insertados es longitud - pos
        inversiones += len(listaOrdenada) - pos
        insort(listaOrdenada, num)
    return inversiones

cantidadDeCasos = int(input())
for _ in range(cantidadDeCasos):
    documentos = list(map(int, input().split()))
    print(contarInversiones(documentos))
