# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и 
# только один раз переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from random import randint

array = []
rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))

if rows * columns % 2 != 0:
    print('Размерность неверная')
else:
    print('Исходный массив:')
    for i in range(rows):
        array.append([randint(1,20) for _ in range(columns)])
        for j in range (columns):
            print(f"{array[i][j]}\t", end ='')       
        print()
    shuffled_positions = [()]
    for i in range(rows*columns//2):
        pos1=()
        while pos1 in shuffled_positions:
            pos1 = (randint(0,rows-1),randint(0,columns-1))
           # print (pos1)
        shuffled_positions.append(pos1)
        pos2=()
        while pos2 in shuffled_positions:
            pos2 = (randint(0,rows-1),randint(0,columns-1))
         #   print (pos2)
        shuffled_positions.append(pos2)
        temp = array[pos1[0]][pos1[1]]
        array[pos1[0]][pos1[1]] = array[pos2[0]][pos2[1]]
        array[pos2[0]][pos2[1]] = temp
    print('Перемешанный массив: ')
    for i in range(rows):
        for j in range (columns):
            print(f"{array[i][j]}\t", end ='')       
        print()







