'''У будинку, що складається з 30 квартир, переселити мешканців так, щоб мешканці першої квартири переїхали в тридцяту,
з тридцятого - в першу, з другої - в 29 і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб. '''
import random

dwellers = [random.randint(1, 7) for x in range(10)]
print('Даний масив жителів:\n', dwellers)

for i in range(10):
    print(f'Кількість жителів в квартирі {i + 1}:', dwellers[i])

moved_dwellers = list(reversed(dwellers))
print('Масив переселених мешканців:\n', moved_dwellers)

for i in range(10):
    print(f'Кількість переселених жителів в квартирі {i + 1}:', moved_dwellers[i])
counter = 0
for j in range(len(moved_dwellers)):
    if moved_dwellers[j] >= 5:
        counter += 1
print('Кількість квартир з більше, ніж 5 жителів:', counter)
