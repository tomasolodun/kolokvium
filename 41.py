'''Змінній t привласнити значення істина, якщо максимальний елемент одновимірного масиву єдиний і не перевищує наперед заданого числа а. '''
import random

array = [random.randint(0, 20) for i in range(20)]
print('Даний масив:\n', array)
a = int(input('Введіть число: '))
t = False
maxElement = max(array)
if array.count((maxElement)) == 1 and maxElement <= a:
    t = True
print(t)
