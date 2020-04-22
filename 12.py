'''Дані про температуру повітря за декаду грудня зберігаються в масиві.
 Визначити, скільки раз температура була вище середньої за цю декаду. '''
import random
n = 10
T = [random.randint(13, 25) for x in range(n)]
print('°C, '.join(map(str, T)), end='°C\n')
count = 0
for i in range(len(T)):
    if T[i] >= 18:
        count += 1
if count == 2 or count == 3 or count == 4:
    print(f'{count} дні, придатних для купання. Т >= 18°C')
else:
    print(f'{count} днів, придатних для купання. Т >= 18°C')