#Tiene mas complejidad que el anterior, porque el anterior era quiera o no pares, pero ahora
#podemos tener numeros impares, por lo que debemos considerar esos espacios.

rInput = int(input())
rList = list(map(str, input().split(", "))) #separados una coma y un espacio

def recorridoArcoiris(rList):
    lenghtList = len(rList)
    newPhrase = []
    for i in range(lenghtList//2):
        wordsList = rList[i]
        wordsListFinal = rList[lenghtList-1-i]
        newPhrase.append(wordsList)
        newPhrase.append(wordsListFinal)
    if isPar(lenghtList)== False:
        newPhrase.append(rList[lenghtList//2])
    return newPhrase

def isPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
finalString = ""

letras = recorridoArcoiris(rList)

for letra in letras:
    finalString += letra

print(finalString)
