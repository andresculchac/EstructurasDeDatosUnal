def isMultiple(numero, multiplo):
    if numero % multiplo == 0:
        return True
    return False



#Resolver el problema cuando empezamos con E
sumM = []
while True:
    a = list(map(str,input().split()))
    multiples = []
    if "E" in a:
        break
    letter, number = a[0] , int(a[1])      
    if (letter == "A"):
        sumM.append(number)
    elif (letter == "M"):
        for i in sumM:
            if isMultiple(i,number):
                multiples.append(i)   
        print(sum(multiples))  




# print(isMultiple(4,3))