'''Знайти добуток елементів масиву цілих чисел, які кратні 7.
Розмірність масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.'''
import random

array = [random.randint(10, 50) for i in range(15)]
print('Даний масив:\n', array)
dob = 1
for j in array:
    if j % 7 == 0:
        dob *= j
if dob > 1:
    print(f'Добуток елементів масиву, кратних 7 дорівнює {dob}')
else:
    print('Таких елементів немає')