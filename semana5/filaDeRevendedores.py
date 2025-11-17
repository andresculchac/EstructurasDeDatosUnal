from collections import deque

firstInput = [3,35]
data = [
    (1001, 3),
    (1002, 3),
    (1003, 3),
    (1004, 3),
    (1005, 3)
]


miDeque = deque()
for i in range(5): #porque son cada 5 integrantes entonces recorre eso.
    miDeque.append(data[i][0])

t = firstInput[1] #35 boletas
#K == son data[1] de cada matriz entonces tenemos que reducir cada uno de ello.
# while t > 0:
#     l = 

''''data[0][1] = y 
    cambio  = t-y
    aqui esta el cambio que tenmos que realizar en el fondo. 
    
'''
print(miDeque)

