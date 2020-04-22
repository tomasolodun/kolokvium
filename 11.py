'''Дані про температуру води на Чорноморському узбережжі за декаду вересня зберігаються в масиві.
 Визначити, скільки за цей час було днів, придатних для купання. '''
import random

T = [random.randint(13, 25) for x in range(10)]
print('°C, '.join(map(str, T)), end='°C\n')
count = 0
for i in range(len(T)):
    if T[i] >= 18:
        count += 1
if count == 2 or count == 3 or count == 4:
    print(f'{count} дні, придатних для купання. Т >= 18°C')
else:
    print(f'{count} днів, придатних для купання. Т >= 18°C')