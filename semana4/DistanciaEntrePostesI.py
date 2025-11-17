outputs = []

requestInput = int(input())

kilometers = list(map(int, input().split()))
bubleSort = sorted(kilometers)
#number of distance between postes
numPostes = int(input())

for i in range(numPostes):
    distanceKm = list(map(int,input().split()))
    sortDistance = sorted(distanceKm)
    minusDifference = sortDistance[1] - sortDistance[0]
    outputs.append(minusDifference)


for _ in outputs:
    print(_,"kms")

#tenemos que asegurar que lo que nos mandan a buscar
#este en la lista que nos dieron, y eso lo encontramos con bisec




