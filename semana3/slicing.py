my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# # sequence[start:stop:step]
# # Get elements from index 2 to 5 (exclusive)
# print(my_list[2:5])  # Output: [2, 3, 4]

# # Get elements from beginning to index 4
# print(my_list[:5])   # Output: [0, 1, 2, 3, 4]

# # Get elements from index 5 to end
# print(my_list[5:])   # Output: [5, 6, 7, 8, 9]

# # Get every other element
# print(my_list[::2])  # Output: [0, 2, 4, 6, 8]

longM = len(my_list) 



def indicateNumbers (i,j):
    if i>0 and j<longM+1:
        mTrue = my_list[(i-1):(j)]
        for i in mTrue:
            print(i, end=" ")


# for i in range(-4,0,1):
#     print(i)

#Slicin inverso de atras para adelante y es mejor que for
D = 3

test =[1,2,3,4]

del test[-D:]

print(test)
