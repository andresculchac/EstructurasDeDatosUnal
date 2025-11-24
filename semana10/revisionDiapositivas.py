#Hacer un codigo con diferentes complejidades
A = [4, 2, 8, 1, 9, 6, 7, 3, 5]
S = 10
valueInt = set()
# for i in range(len(A)): #len(A) = 9
#     o = A[0] + A[i]
#     print(o)

#Hecho por mi

# for j in A:
#     valueInt.add(j)
#     for i in range(len(A)):
#         if A[i] != j:
#             if A[i] in valueInt:
#                 continue
#             else:
#                 l = j + A[i]
#                 print("la suma de eles cuando", j , A[i])
#                 if l == 10:
#                     print(l)

#el problema de este codigo es que los valores ya no se
#pueden repetir, entonces por 2 y 8 sale un valor
# y por 8 y 2 que ya salio vuelve y sale un conteo

#Fuerza bruta diapositivas

# def dosSumas(A,S):
#     c = 0
#     N = len(A)
#     for i in range(0,N-1):
#         for j in range(i+1, N-1):
#             print("las sumas son", A[i], A[j])
#             if A[i] + A[j] == 10:
#                 c +=1
#     return c

# print(dosSumas(A,S))


#Now hashing set, efficient form

def dosSumas(A,S):
    c = 0
    B = set(A)
    N = len(A)
    for i in range(0, N-1):
        if A[i] != S/2 and (S - A[i]) in B:
            c += 1
    return c//2       

print(dosSumas(A,S))