'''Перетин даху має форму півкола з радіусом R м.
 Сформувати таблицю, яка містить довжини опор, які встановлюються через кожні R / 5 м. '''
import math
radius = int(input('Введіть радіус: '))
distance = radius / 5
x = 0
i = 0
while x < 2 * radius - distance:
    x += distance
    i += 1
    print(f'{i} = ',math.sqrt(x * (2 * radius - x)))