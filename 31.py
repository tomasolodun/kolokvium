'''Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які потрапляють в інтервал від -2 до 10. '''
import random

array = [random.randint(-10, 20) for i in range(20)]
print('Даний масив:\n', array)
sum = 0
counter = 0
for i in range(len(array)):
    if -2 <= array[i] <= 10:
        sum += array[i]
        counter += 1
print("Середнє арифметичне значення тих елементів одновимірного масиву, які потрапляють в інтервал від -2 до 10 = ",
      sum / counter)
