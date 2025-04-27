#Quiero simplificar el programa, ademas de encontrar el error que me da en las sumas
#Entiendo porque un codigo largo es dificil de leer, la importancia de hacer un codigo limpio y entendible
#so lar is. Estoy creando 3 variables, pero puedo simplificarlo en una lista

def sumasTotales(list, intIntentos): 
    ptsJugadores = [0,0,0]
    
    for i in range(intIntentos):
        sumatorias = [] 
        for j in range(3):
            sumaMainTuple = list[j][i]
            sumatorias.append(sumaMainTuple)
        paridad = isPar(sum(sumatorias)) #necesito recorrer para los tres jugadores

        for y in range(3):
            intentoJugador = isPar(sumatorias[y])
            if paridad == intentoJugador:
                ptsJugadores[y] += 1
    
    return ptsJugadores[0], ptsJugadores[1], ptsJugadores[2] #SO, LAR, IS
def isPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


rInput = int(input())
mainTuple = []

for i in range(3): #Recibir la entrada predeterminada (3 participantes)
    c = list(map(int, input().split(", ")))
    mainTuple.append(c)




so, lar, iS = sumasTotales(mainTuple,rInput)
print(f"SO:{so}, LAR:{lar}, IS:{iS}")

