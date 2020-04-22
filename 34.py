'''Дано два лінійних масиви однакової розмірності.
 Скласти третій масив з добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.'''
import random

array1 = [random.randint(1, 20) for i in range(20)]
array2 = [random.randint(1, 20) for i in range(20)]
array3 = [array1[i]*array2[i] for i in range(len(array1))]
print('Перший масив:\n',array1)
print('Другий масив:\n',array2)
print('Складений масив:\n',array3)
