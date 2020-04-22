'''Знайти кількість парних елементів одновимірного масиву. '''
import random

array = [random.randint(10, 100) for i in range(10)]
print('Даний масив:\n', array)
counter = 0
for j in array:
    if j % 2 == 0:
        counter += 1
print(f'Кількість парних елементів масиву дорівнює {counter}')
