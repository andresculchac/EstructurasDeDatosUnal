def repartir (integrantes:int, size:int, billetes:list):
    numbersIntegranes = [0]*integrantes
    for i in range(size):
        equally = i % integrantes
        numbersIntegranes[equally] += billetes[i]
    result = max(numbersIntegranes) - min(numbersIntegranes)
    return result

inputCases = int(input())

for _ in range(inputCases):
    integrantesBilletes= list(map(int, input().split()))
    billetesAndMoney = list(map(int, input().split()))
    output = repartir(integrantesBilletes[0],integrantesBilletes[1],billetesAndMoney)
    print(output)

#hecho en onenote la parte analitica

    