'''Задано два натуральних числа a і b.
Змінній w привласнити значення істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а і не кратний b.  '''
import random

array = [random.randint(0, 20) for i in range(20)]
print('Даний масив:\n', array)
a = int(input('Введіть a:'))
b = int(input('Введіть b:'))
w = False
for i in array:
    if i % a == 0 and i % b != 0:
        w = True
        break
print(w)