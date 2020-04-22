'''Створіть масив А [1..12] за допомогою генератора випадкових чисел з елементами від -20 до 10 і виведіть його на екран.
 Замініть всі від’ємні елементи масиву числом 0.'''
import random

array = [random.randint(-20, 10) for i in range(12)]
print('Даний масив:\n', array)
for j in range(len(array)):
    if array[j] < 0:
        array[j] = 0
print('Новий масив:\n ', array)
