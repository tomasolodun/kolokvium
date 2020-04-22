'''Змінній t привласнити значення істина, якщо в одновимірному масиві є хоча б одне від’ємне і парне число. '''
import random

array = [random.randint(-10, 20) for i in range(10)]
print('Даний масив:\n', array)
t = False
for i in range(len(array)):
    if array[i] % 2 == 0 and array[i] < 0:
        t = True
        break
print(t)