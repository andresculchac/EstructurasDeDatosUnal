welcome = []

dictionary = dict()
request = int(input())
for i in range(request):
    ewoke,translate = list(map(str, input().split()))
    dictionary[ewoke] = translate
while True: 
    request1 = input()
    if request1 == "#":
        break
    elif request1 in dictionary:
            welcome.append(dictionary[request1])
    else:
        welcome.append("Entrada no encontrada")


for w in welcome:
    print(w)
