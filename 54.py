'''Введіть масив з 20 елементів і визначте, чи є в ньому елементи з однаковими значеннями. '''
import random

array = [random.randint(0, 50) for i in range(20)]
print('Даний масив:\n', array)
if len(array) != len(set(array)):
    print("Присутні елементи з однаковими значеннями.")
else:
    print("Усі елементи унікальні.")