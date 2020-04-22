'''Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які розташовані за першим по порядку
мінімальним елементом. '''
import random

array = [random.randint(10, 100) for i in range(10)]
print('Даний масив:\n', array)
minIndex = array.index(min(array))
amount = 0
counter = 0
for i in range(minIndex, len(array)):
    amount += array[i]
    counter += 1
print(f'Середенє арифметичне значення тих елементів одновимірного масиву, '
      f'які розташовані за першим по порядку мінімальним елементом ({min(array)}) =  {amount / counter}')
