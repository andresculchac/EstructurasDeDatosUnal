numbers = []
outputN = []
while True:
    longN = len(numbers) #creo que seria mejor meterlo en 
    inputN = list(map(str, input().split())) #List str = [0,9]
    firstN = inputN[0]
    if 'end' in inputN[0]:
        break
    else:
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
            numbers.pop(-1)
        elif firstN == "D":
            if int(inputN[1]) <= longN:
                for i in range((-int(inputN[1])),0,1):
                    numbers.pop(i)

for i in outputN:
    print(int(i))
