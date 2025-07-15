numbers = []
outputN = []
while True:
    longN = len(numbers)
    inputN = list(map(str, input().split())) #List str = [0,9]
    firstN = inputN[0]
    if 'end' in inputN[0]:
            break
    if len(firstN) == 1 :
        if  (48<=ord(firstN)<= 57):
                numbers.append(firstN)
        elif firstN == "M":
            i = int(inputN[1])
            j = int(inputN[2])
            if i>0 and j<=longN:
                showN = numbers[(i-1):(j)]
                result = ''.join(str(i) for i in showN)
                outputN.append(result)               
        elif firstN == "C":
            if numbers:
                numbers.pop(-1)
        elif firstN == "D":
            if  1 <=int(inputN[1]) <= longN:
                del numbers[-int(inputN[1]):]

for i in outputN:
    print(i)

#de este hpta problema aprendi que debemos agregar todos los condicionales, y ademas tener en cuenta el pop, 
#por que si en algun momento estan vacias las listas o algo relacionado entonces queee!