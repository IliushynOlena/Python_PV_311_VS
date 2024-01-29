matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matrix)
# for item in matrix:
#     for num in item:
#        print(num, end=" ")
#     print()
    
# print(matrix[0][0])
# print(matrix[1][1])

for i in range(len(matrix)):# len =  3 
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

arr = [[j for j in range(5)] for i in range(5)]   
print(arr)
for i in range(len(arr)):# len =  3 
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

import random
matrix = []
row = 3
col = 4
# for i in range(row):
#     number = []
#     for j in range(col):
#         number.append(random.randint(10,50))
#     matrix.append(number)

for i in range(row):
    matrix.append([random.randint(10,50) for i in range(col)])
    
for i in range(len(matrix)):# len =  3 
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
    
summa = 0
for row in matrix:
    summa+= sum(row)
    print(f'Summa {row} row : {sum(row)}')
print(f'Summa = {summa}')

#Створити квадратну матрицю…кількість рядків і колонок вводить 
# користувач з клавіатури
#Знайти суму елементів розташованих на головній та бічній діагоналі

row = 3
col = 3
sum_main = 0
sum_2 = 0
matrix = []
for i in range(row):
    matrix.append([random.randint(1,10) for i in range(col)])
    
for i in range(len(matrix)):# len =  3 
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
    
for i in range(row):
    sum_main+= matrix[i][i]
    sum_2 += matrix[i][col-1 -i]
    
print(f'Summa main axis {sum_main}')
print(f'Summa main axis {sum_2}')

