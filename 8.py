'''Створіть цілочисельний масив А [1..15] за допомогою генератора випадкових чисел з елементами від -15 до 30 і виведіть його на екран.
Визначте найбільший елемент масиву і його індекс. '''
import random

array = [random.randint(-15, 30) for i in range(15)]
print('Даний масив:\n', array)
max = 0
k = 0
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        k = i
print(f'Найбільший елемент масиву - {max}[{k}]')