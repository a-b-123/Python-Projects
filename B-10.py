#2-D lists
#2-d list is using a list within a list. 
numbergrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#created a grid like structure with 4 rows and 3 columns
#accessing individual elements within 2-d list:
#listname[row index #][index of column]]
print(numbergrid[0][0]) #will return 1
print(numbergrid[2][1]) #will return 8

#nested for loop to access elements in 2-d list:
for row in numbergrid: #accessing each list
    for col in row: #accessing elements in each list
        print(col)