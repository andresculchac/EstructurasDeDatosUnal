pedir = int(input())
listNum = []
numero = input()
aa = numero.split(" ")
for i in aa:
    listNum.append(int(i))

print(listNum)

sizeListNum = (len(listNum))*-1

##print(sizeListNum)
contador = 0
for i in range(-1,sizeListNum-1,-1):
    if i == -1:
        contador += listNum[i]
    else:
        contador += listNum[i]
        print(contador)
        