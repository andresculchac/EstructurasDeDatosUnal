#hecho por AI


InputEntrada = int(input())
for _ in range(InputEntrada):
    inputInicial = list(map(int, input().split()))
    guardarCode = {}
    for x in inputInicial:
        if x in guardarCode:
            guardarCode[x] += 1
        else:
            guardarCode[x] = 1
    res = []
    for key in sorted(guardarCode):
        res.append(str(guardarCode[key]))
    print(' '.join(res))
