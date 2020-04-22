'''Дано одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних чисел в ньому. '''
import random

array = [random.randint(0, 10) for i in range(10)]
print('Даний масив:\n', array)
print('Кількість різних чисел в даному масиві:',len(set(array)))