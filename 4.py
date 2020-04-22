'''Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які починаються з певної букви, яка вводиться з клавіатури. '''
n = 5
array = [(input()) for i in range(n)]
print(array)
letter = input('Введіть букву,з якої починається прізвище')
for i in range(n):
    if letter in array[i][0]:
        print(array[i])
    else:
        print('Прізвищ на дану букву немає')
