# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint

size = int(input('Введите количество элементов: '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

sequence = [randint(1,20) for _ in range(size)]
print (sequence)

print("Искомые индексы:", end = ' ')
for i in range(size):
    if sequence[i] >= min and sequence[i] <= max:
        print(i, end = ' ')
