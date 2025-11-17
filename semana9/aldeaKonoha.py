PopulationKonoha = set()

while True:
    request = list(map(str, input().split()))
    if request[0] == "B":
        if request[1] in PopulationKonoha: #Error porque ya nació
            continue
        else:
            PopulationKonoha.add(request[1])
    elif request[0] == "D":
        PopulationKonoha.discard(request[1])
    elif request[0] == "R":
        if request[1] in PopulationKonoha:
            continue
        else:
            PopulationKonoha.add(request[1])
    else:
        break


print(len(PopulationKonoha))
print(PopulationKonoha)
