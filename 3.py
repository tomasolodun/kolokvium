'''Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком, починаючи з останнього. '''
n = 5
array = [(input()) for i in range(n)]
print(array)
for i in range(n):
    print(array[n - i - 1], end="\n")
