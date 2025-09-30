r = int(input())
for _ in range(r):
    code = input().split() 
    n = len(code)

    
    for i in range(n // 2):
        code[i], code[n - 1 - i] = code[n - 1 - i], code[i]
    for i in range(0, n - 1, 2):
        code[i], code[i + 1] = code[i + 1], code[i]
    print(''.join(code))


