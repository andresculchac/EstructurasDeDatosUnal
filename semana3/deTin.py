def tin(N,K):
    students = [i for i in range(1,N+1)] #[1,2,3,4,5]
    inicio = 0
    while N != 1:
        u = (inicio + K) % N
        inicio = u-1
        cleanP = students.pop(inicio)   
        N = len(students)
        K = cleanP % N
        if K == 0:
            K = 1
    return students[0]


nCases = int(input())

for _ in range(nCases):
    a = list(map(int, input().split()))
    resultado = tin(a[0],a[1])
    print(resultado)







