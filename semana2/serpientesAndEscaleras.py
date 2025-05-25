turnos = 0
index = set()   #para encontrar respuestas O(1)
listTurn = [3, -1, 4, -2]
initialTurn = 0
while True:
    algorithm =  initialTurn + listTurn[initialTurn]
    #comencemos por los turnos
    if algorithm < 0 or algorithm >= len(listTurn):
        break
    #agregar el if cuando se repite la casilla
    if algorithm in index:
        break
    turnos += 1 #contabilizamos turnos
    #rapidamente nos ponemos en la posicion de la primera lista, falta lo interactivo
    index.add(algorithm)
    initialTurn = algorithm
print(turnos)    
     