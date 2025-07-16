numbers = []


while True:
    squid = int(input())
    if squid <5000:
        if squid == 0:
            break
        numbers.append(squid)



winner = []
for i in numbers:
    if i > 0:
        if i in winner:
            winner.remove(i)
        elif i+1 in winner:
            winner.remove(i+1)
        elif i-1 in winner:
            winner.remove(i-1)
        else:
            winner.append(i)
if not winner:
    print(0)
else:
    print(*winner)



