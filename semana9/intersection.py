a = [1,2,3,4,5,6,7]
b = [7,8,9,10,11,12,13]

#function search 
#As a result will be 7
convert = set(a)
intersection = set()

for i in range(len(b)):
    if b[i] in convert:
        intersection.add(b[i])

print(intersection)






