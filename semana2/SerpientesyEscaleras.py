def snakeLadder(long:int,lista:list):
    saltos = 1
    while True:
        splash = lista[saltos-1]
        if lista[splash-1] == 0:
            return saltos
        if lista[splash-1] >= long or lista[splash-1] < 0:
            return splash
        
        elif saltos < long :
            saltos += splash
        elif saltos >= long:
            return saltos

# num_cases = int(input())
# for i in range(num_cases):
#     long = int(input())
#     lista = list(map(int, input().split()))
#     print(snakeLadder(long, lista))

print(snakeLadder(4, [1,1,1,0]))
#a este tema le falta las posiciones en las que quedamos, le falta tambien 
#aprender a identificar las restricciones
