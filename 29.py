'''Знайти кількість парних елементів одновимірного масиву до першого зустрінутого числа рівного наперед заданому числу а. '''
import random

array = [random.randint(10, 100) for i in range(10)]
print('Даний масив:\n', array)
array_filtered = list(filter(lambda i: i % 2 == 0, array))
print('Відфільтрований масив:\n', array_filtered)
a = int(input('Введіть стоп-число: '))
array_stopped = []
for i in range(len(array_filtered)):
    if array_filtered[i] != a:
        array_stopped.append(array_filtered[i])
    else:
        break
print('Масив чисел до Вашого стоп-числа:\n', array_stopped, f'\nКількість елементів: {len(array_stopped)} ')