'''Дано одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому повторюється найчастіше число. '''
import random

array = [random.randint(0, 10) for i in range(20)]
print('Даний масив:\n', array)
maxCount = 0
elem = None
for i in array:
    if array.count(i) > maxCount:
        maxCount = array.count(i)
        elem = i
if maxCount == 2 or maxCount == 3 or maxCount == 4:
    print(f'Елемент {elem} повторюється {maxCount} рази')
else:
    print(f'Елемент {elem} повторюється {maxCount} разів')