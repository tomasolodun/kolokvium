'''У лінійному масиві знайти максимальний елемент.
Вставте порядковий номер елемента за ним, пересунувши всі залишилися на одну позицію вправо. '''
import random

array = [random.randint(10, 100) for i in range(10)]
print('Даний масив:\n', array)
maxElemIndex = array.index(max(array))
array.insert(maxElemIndex+1, maxElemIndex)

print('Новий масив:\n',array)