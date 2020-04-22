'''Якщо в одновимірному масиві є три поспіль однакових елемента, то змінній r привласнити значення істина. '''
import random

array = [random.randint(0, 5) for i in range(20)]
print('Даний масив:\n', array)
r = False
for i in range(0,len(array)-2):
    if array[i] == array[i + 1] == array[i + 2]:
        r = True
        break
print('Чи є в даному масиві три поспіль однакових елементи: ',r)