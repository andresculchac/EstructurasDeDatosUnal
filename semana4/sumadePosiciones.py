
from bisect import bisect_left
outputs = []

firstInput = int(input())
for _ in range(firstInput):
    desSorting = list(map(int,input().split()))
    arr = sorted(desSorting)
    mompyrri = {}

    for x in arr:
        if x in mompyrri:
            mompyrri[x] += 1
        else:
            mompyrri[x] = 1

    outputs.append(list(mompyrri.values()))


for lista in outputs:
    print(*lista)





