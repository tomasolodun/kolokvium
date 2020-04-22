'''Підрахуйте кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3. '''
import random

array = [random.randint(0, 100) for i in range(100)]
print('Даний масив:\n', array)
counter = 0
for i in range(len(array)):
    if array[i] == i and array[i] % 3 == 0:
        counter += 1

print('Кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3: ',counter)