'''Дані про температуру повітря і кількості опадів за декаду квітня зберігаються в масивах.
Визначити кількість опадів, що випали у вигляді дощу і у вигляді снігу за цю декаду. '''
import random
info = [[random.randint(-20, 10), random.randint(0, 50)] for i in range(10)]
print(info)
snow = 0
rain = 0
for i in info:
    if i[0] <= 0:
        snow += i[1]
    else:
        rain += i[1]
print('Кількість опадів, що випали у вигляді снігу за декаду квітня:',snow)
print('Кількість опадів, що випали у вигляді дощу за декаду квітня:',rain)