'''Створіть масив з 15 цілочисельних елементів і визначте серед них мінімальне значення.'''
import random

array = [random.randint(-30, 30) for i in range(15)]
print('Даний масив:\n', array)
print('Мінімальне значення', min(array))
