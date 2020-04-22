'''Дано одновимірний масив а. Сформувати новий масив, який складається тільки з тих елементів масиву а, які перевищують свій номер на 10.
Якщо таких елементів немає, то видати повідомлення. '''
import random

array = [random.randint(0, 100) for i in range(100)]
print('Даний масив:\n', array)
newArray = []
for i in range(len(array)):
    if array[i] - i == 10:
        newArray.append(array[i])
if len(newArray) == 0:
    print("Помилка,таких елементів немає.")
else:
    print(newArray)