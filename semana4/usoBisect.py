import bisect
edades = [5, 12, 15, 20, 25, 30, 40]

edad18 = bisect.bisect_left(edades,18)
edad20 = bisect.bisect_left(edades,20)
edades.insert(edad18,18)
edades.insert(edad20,20)
print(edades)
