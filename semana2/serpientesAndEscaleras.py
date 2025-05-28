turnos = 0
index = {0}   #para encontrar respuestas O(1)
listTurn = [1]
initialTurn = 0
while True:
    algorithm =  initialTurn + listTurn[initialTurn]
    turnos += 1 #contabilizamos turnos
    #comencemos por los turnos
    if algorithm < 0 or algorithm >= len(listTurn) or algorithm in index:
        break
    #rapidamente nos ponemos en la posicion de la primera lista, falta lo interactivo
    index.add(algorithm)
    initialTurn = algorithm
print(turnos)    
     
     