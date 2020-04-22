'''Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки за ці послуги.
 Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.'''
from random import randint

serviceNames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [randint(0, 100) for i in range(10)]
print('Послуги: ',serviceNames)
print('Ціни: ',price)
G = int(input('Введіть ціну зі списку: '))
if G in price:
    counter = price.index(G) - 1
    while counter >= 0:
        serviceNames.pop(0)
        price.pop(0)
        counter -= 1
print('Послуги2: ',serviceNames)
print('Ціни2: ',price)