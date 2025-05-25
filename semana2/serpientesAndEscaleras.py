def Solve():
    CaseCount = int(input())
    Answers = []
    for _ in range(CaseCount):
        TurnQty = int(input())
        ListTurn = list(map(int, input().split()))
        TurnCounter = 0
        Visited = set()
        Current = 0
        while True:
            Next = Current + ListTurn[Current]
            if Next < 0 or Next >= len(ListTurn):
                break
            if Next in Visited:
                break
            TurnCounter += 1
            Visited.add(Next)
            Current = Next
        Answers.append(TurnCounter)
    for Value in Answers:
        print(Value)


if __name__ == "__main__":
    Solve()
