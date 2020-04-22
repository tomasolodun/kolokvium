'''Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8 одночасно.
Розмірність масиву - 30. Заповнення масиву здійснити випадковими числами від 500 до 1000. '''
import random

array = [random.randint(500, 1000) for i in range(30)]
print('Даний масив:\n', array)
sum = 0
for j in array:
    if j % 5 == 0 and j % 8 == 0:
        sum += j
print(f'Сума елементів масиву цілих чисел, які діляться на 5 і на 8 одночасно {sum}')