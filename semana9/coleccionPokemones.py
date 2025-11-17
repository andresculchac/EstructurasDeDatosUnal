# V = [13, 10, 14, 13]
# F = [12, 10, 11]

# vanesa = set(V)
# felipe = set(F)

# print(vanesa & felipe)
# print(vanesa | felipe)
# print(vanesa - felipe)
# print(vanesa ^ felipe)
# print("tamaño de vanesa", len(vanesa))
# print("tamaño de felipe", len(felipe))

#Entrada

vanesa = set()
felipe = set()

while True:
    request = list(map(str, input().split()))
    if request[0] == "V":
        vanesa.add(request[1])
    elif request[0] == "F":
        felipe.add(request[1])
    elif request[0] == "#":
        break

# print("como se ve el string", vanesa)
# print("como se ve el string", felipe)

print(len(felipe),len(vanesa),len(felipe | vanesa) )
