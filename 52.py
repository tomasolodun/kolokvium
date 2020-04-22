'''Знайти найбільший елемент з елементів одновимірного масиву, що мають парний номер. Визначити, чи є він єдиним. '''
import random

array = [random.randint(0, 100) for i in range(100)]
print(array)
evenElements = []
for i in range(len(array)):
    if i % 2 == 0:
        evenElements.append(array[i])

maximalElement = max(evenElements)
unique = False
if array.count(maximalElement) == 1:
    unique = True
print("Найбільший елемент =",maximalElement, "Чи є унікальним =",unique)