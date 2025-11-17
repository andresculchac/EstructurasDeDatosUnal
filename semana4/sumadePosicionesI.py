from bisect import bisect_left

inputFirst = int(input())
a = tuple(map(int, input().split()))
inputSnd = int(input())
b = tuple(map(int, input().split()))


sumAll = 0
for i in b:
    al = bisect_left(a, i)
    if al < len(a) and a[al] == i:
        sumAll += al + 1


print(sumAll)


    


