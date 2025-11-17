from bisect import bisect_left


def divisores():
        divisor = []
        for i in range(1,p+1):
            if p%i == 0:
                a = bisect_left(c,i)
                if c[a] == i and i not in divisor:
                    divisor.append(i)
                else:
                    return False
        return True
listAllResults = []
firstInput = int(input())

for i in range(firstInput):
    candP = list(map(int,input().split()))
    c = tuple(map(int, input().split()))
    p = candP[1]
    listAllResults.append(divisores())


    

for x in listAllResults:
    if x:
        print("Es PrimiConjunto")
    else:
         print("No es PrimiConjunto")

#debemos asegurar cuando la lista este vacia o no
# asegurar que los numeros no se repitan         