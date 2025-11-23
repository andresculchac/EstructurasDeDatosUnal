vivos = set()
muertos = set()

while True: 
    request = list(map(str, input().split()))
    if request[0] == "E": #primero el break
        break
    if request[0] == "B":
        if request[1]not in vivos and request[1] not in muertos:
            vivos.add(request[1])
    elif request[0] == "D":
        if request[1]  in vivos:
            muertos.add(request[1])
            vivos.remove(request[1])
    elif request[0] =="R":
        if request[1] in muertos:
            muertos.remove(request[1])
            vivos.add(request[1])



print(len(vivos))