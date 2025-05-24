def saltoMagico(tablero):
    visitado=[False]*len(tablero)
    posicion=0
    totalSaltos=0

    while 0<=posicion<len(tablero) and not visitado[posicion]:
        visitado[posicion]=True
        posicion+=tablero[posicion]
        totalSaltos+=1
    return totalSaltos


def iniciaJuego():
    casos=int(input())
    respuestas=[]
    for _ in range(casos):
        _=int(input())
        tablero=list(map(int,input().split()))
        respuestas.append(str(saltoMagico(tablero)))
    print("\n".join(respuestas))


iniciaJuego()