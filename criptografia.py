# rInput = int(input())

# for i in range(rInput):
#     fistCrypto = list(map(int, input().split(" "))) #separados por los espacios en blanco
#     secondCrypto = list(map(int, input().split(" "))) #separados por los espacios en blanco	


def isOddNumber(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
def DecodeCrypto(code):
    for i in range(len(code)):
        if isOddNumber(i):
            change1 = code[i-1] = code[i-1] + 1
            change2 = code[i] = code[i] - 1
            

    return code

my_list = ['i', 'a', 'f', 'g', 'r', 't', 'o', 'i', 'p', 'c', 'r']
print(DecodeCrypto(my_list))

