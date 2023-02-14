# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint

array = []
rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))

print('Исходный массив:')
for i in range(rows):
    array.append([randint(1,20) for _ in range(columns)])
    for j in range (columns):
        print(f"{array[i][j]}\t", end ='')       
    print()

num_list = [0]*20
for i in range(rows):
    for j in range(columns):
        num_list[array[i][j]-1] +=1
      
current_number = 0
for i in range(rows):
    for j in range(columns):
        while num_list[current_number] == 0:
            current_number +=1
        array[i][j] = current_number+1
        num_list[current_number] -=1

print('Отсортированный массив: ')
for i in range(rows):
    for j in range (columns):
        print(f"{array[i][j]}\t", end ='')       
    print()





