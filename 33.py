'''Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів. '''
import random

A = [random.randint(-2, 2) for i in range(20)]
print('Даний масив:\n', A)
dob = 1
for i in range(len(A)):
    if A[i] != 0:
        dob *= A[i]
if dob > 1:
    print('Добуток всіх ненульових елементів масиву =',dob)
else:
    print('Таких елементів немає')