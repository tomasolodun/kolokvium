'''Знайти суму всіх елементів масиву дійсних чисел, більших за задане число.
 Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 50 до 100.'''
import random

A = [random.uniform(50, 100) for i in range(20)]
print('Даний масив:\n', A)
B = int(input('Введіть число: '))
sum = 0
for j in A:
    if j > B:
        sum += j
print(f'Cумa всіх елементів масиву дійсних чисел, більших за {B} дорівнює {sum}')
