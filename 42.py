'''Підрахувати кількість елементів одновимірного масиву, для яких виконується нерівність i*i<ai<i! '''
import random
import math

array = [random.randint(0, 10) for i in range(20)]
print('Даний масив:\n', array)
counter = 0
for i in range(len(array)):
    if i**2 < array[i] < math.factorial(i):
        counter += 1

print('Кількість елементів одновимірного масиву, для яких виконується нерівність i*i<i<i! :',counter)