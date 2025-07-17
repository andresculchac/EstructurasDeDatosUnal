multiple = int(input())
counter = 0
numbers = []
while True: 
    counter += 1
    number = int(input())
    if number == 0:
        break
    numbers.append(number)
    if counter % 5 == 0:
        numbers.sort()
        longNumbers = len(numbers)
        if longNumbers % 2 != 0:        #find the medium index
            median = numbers[longNumbers//2]
            print(median)
        else:
            median = numbers[int(longNumbers)/2] + numbers[(int(longNumbers)/2)+1]
            print(median,'/2')



