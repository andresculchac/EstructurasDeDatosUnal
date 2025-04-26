def sumasTotales(list, intIntentos):
    sumatorias = []
    jugadores = []
    so = 0
    lar = 0
    iS = 0
    for i in range(intIntentos): 
        contador = 0
        for j in range(3):#Son 3 participantes
            sumaMainTuple = list[j][i]
            jugadores.append(isPar(sumaMainTuple)) # Agregar la suma de cada columna a la lista
            contador += sumaMainTuple
        sumatorias.append(isPar(contador)) # Agregar la suma de cada columna a la lista
    for i in range(3): # Son 3 participantes
        for s in sumatorias:
            if i == 0:
                if jugadores[0] and s:
                    so += 1
                elif jugadores[0] == False and s == False:
                    so += 1
            if i == 1:
                if jugadores[1] and s:
                    lar += 1
                elif jugadores[1] == False and s == False:
                    lar += 1
            if i == 2:
                if jugadores[2] and s:
                    iS += 1
                elif jugadores[2] == False and s == False:
                    iS += 1

    return so, lar, iS
def isPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


rInput = int(input())
mainTuple = []

for i in range(3): # Son 3 participantes
    c = list(map(int, input().split(",")))
    mainTuple.append(c)

so, lar, iS = sumasTotales(mainTuple,rInput)
print(f"SO:{so}, LAR:{lar}, IS:{iS}")

