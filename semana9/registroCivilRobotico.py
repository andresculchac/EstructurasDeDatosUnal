
f = int(input())
newSet = set(range(1,f+1))
output = []

while True:
    request = list(map(str, (input().split())))
    SearchOrNew = request[0]
    if SearchOrNew == "#":
        break
    elif SearchOrNew == "new":
        first = int(request[1])
        second = int(request[2])
        sumRobots = first+second
        if sumRobots in newSet:
            while True:
                sumRobots += 1
                if sumRobots not in newSet:
                    newSet.add(sumRobots)
                    break
        else:
            newSet.add(sumRobots)
    elif SearchOrNew == "search":
        searchInt = int(request[1])
        if searchInt in newSet:
            output.append("existe")
        else:
            output.append("no existe")

for i in output:
    print(i)
