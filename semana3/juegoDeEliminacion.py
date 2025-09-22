game = []

while True:
    N = int(input())
    if N == 0:
        break
    if N in game:
        game.remove(N)
        continue
    if N+1 in game:
        game.remove(N+1)
        continue
    if N-1 in game:
        game.remove(N-1)
        continue
    game.append(N)

if len(game) == 0:
    print(0)
else:
    print(*game)

    
