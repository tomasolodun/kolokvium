'''Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до 100. '''
import random

array = [random.randint(10, 100) for i in range(10)]
print('Даний масив:\n', array)
dob = 1
for j in array:
    if j % 5 == 0:
        dob *= j
if dob > 1:
    print(f'Добуток елементів масиву, кратних 5 дорівнює {dob}')
else:
    print('Таких елементів немає')