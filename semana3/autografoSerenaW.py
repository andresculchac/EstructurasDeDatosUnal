demoTest = []
letters = []
while True:
    requestInput = list(map(str, input().split()))
    if requestInput[0] in letters or len(requestInput[0])>6:
        continue
    if requestInput[0] == '0' and requestInput[1] == '0':
        break
    demoTest.append(int(requestInput[1]))
    letters.append(requestInput[0])

#Vamos a trabajar con una lista, suponiendo que no importa las letras


#No abra mas de una linea con la misma identificacion
fansRow = []


for i in demoTest:
    longFansRow = len(fansRow)
    lastRemove = []
    if i > longFansRow: #El fan define su max y decide si se forma
        fansRow.append(i)
        longFansRow = len(fansRow)
    
    for j in fansRow:    
        if j < longFansRow:
            lastRemove.append(j)
    if len(lastRemove) > 0:
        fansRow.remove(lastRemove[-1])

print((len(fansRow)))
    
    
    




        
    
