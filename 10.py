'''Дані про температуру повітря за декаду листопада зберігаються в масиві.
 Визначити, скільки разів температура опускалася нижче -10 градусів. '''
import random

T = [random.randint(-20, 10) for x in range(10)]
print('°C, '.join(map(str, T)), end='°C\n')
count = 0
for i in range(len(T)):
    if T[i] < -10:
        count += 1
if count == 2 or count == 3 or count == 4:
    print(f'{count} рази температура опускалася нижче -10°C ')
else:
    print(f'{count} разів температура опускалася нижче -10°C ')