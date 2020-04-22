'''Дано лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по спаданню.'''
import random

array = [random.randint(1, 10) for i in range(10)]
print('Даний масив:\n', array)
sortedArray = sorted(array)
sortedArray.reverse()
if array == sortedArray:
    print(True)
else:
    print(False)