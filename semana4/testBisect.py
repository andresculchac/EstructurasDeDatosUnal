from bisect import bisect_left
numbers = [20,30,10,20]
a = sorted(numbers)
print("lista Ordenanda",a)
print(bisect_left(a, 30))

