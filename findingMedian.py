multiple = int(input())
counter = 0
numbers = []
container = []
while True: 
    number = int(input())
    if number == 0:
        break
    counter += 1
    numbers.append(number)
    if counter % multiple == 0:
        numbers.sort()
        longNumbers = len(numbers)
        if longNumbers % 2 != 0: #Odd        #find the medium index
            median = numbers[longNumbers//2]
            container.append(median)
        else:
            median = numbers[longNumbers//2 - 1 : longNumbers//2 + 1]
            sumFind = sum(median)
            if sumFind % 2 == 1:
                medianFinding =str(sum(median))+"/2"
                container.append(medianFinding)
            else:
                container.append(sumFind/2)

for i in container:
    print(str(i))
