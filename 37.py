'''Розсортуйте заданий лінійний масив по зростанню. '''
import random

array = [random.randint(1, 100) for i in range(30)]
print('Даний масив:\n', array)
print('Розсортований заданий масив за зростанням:\n',sorted(array))