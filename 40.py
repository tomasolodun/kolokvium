'''Обчислити суму парних елементів одновимірного масиву до першого зустрінутого нульового елемента. '''
import random

array = [random.randint(0, 10) for i in range(30)]
print('Даний масив:\n', array)
array_filtered = list(filter(lambda i: i % 2 == 0, array))
print('Відфільтрований масив:\n', array_filtered)
sum = 0
for i in array:
    if i == 0:
        break
    if i % 2 == 0:
        sum += i

print('Суму парних елементів одновимірного масиву до першого зустрінутого нульового елемента',sum)