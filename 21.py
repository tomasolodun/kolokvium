'''Знайти добуток всіх елементів масиву дійсних чисел, менших заданого числа.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 50 до 100. '''
import random

A = [random.uniform(50, 100) for i in range(10)]
print('Даний масив:\n', A)
B = int(input('Введіть число: '))
dob = 1
for j in A:
    if j < B:
        dob *= j
if dob > 1:
    print(f'Добуток всіх елементів масиву дійсних чисел, менших за {B} дорівнює {dob}')
else:
    print('Таких елементів немає')