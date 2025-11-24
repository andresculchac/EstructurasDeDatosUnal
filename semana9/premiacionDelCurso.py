# grupo1 = {1000001, 1000002, 1000003}

# grupo2 = {1000002, 1000004, 1000001, 1000003}

# grupo3 = {1000001, 1000003}

# grupo4 = {1000003, 1000001}

# grupo5 = {1000005, 1000001, 1000004, 1000002, 1000003}


# members = grupo1 & grupo2 & grupo3 & grupo4 & grupo5
# print(members)
# reward = 1000000


grupos = [set() for _ in range(5)]

for i in range(5):
    request = int(input())
    for j in range(request):
        secondR = int(input())
        grupos[i].add(secondR)

splitReward = grupos[0] & grupos[1] & grupos[2] & grupos[3] & grupos[4]

if len(splitReward) == 0:
    print("Nadie gana")
else:
    reward = 1000000
    splitEqual = reward / len(splitReward)
    print(int(splitEqual))

