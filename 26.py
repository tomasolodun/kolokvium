'''Напишіть програму аналізу значень температури хворого за добу: визначте мінімальне і максимальне значення, середнє арифметичне.
Заміри температури виробляються шість раз на добу і результати вводяться з клавіатури у масив T.'''
T = [float(input(f'Введіть {i + 1} елемент: ')) for i in range(6)]
print('Заміри:\n','°C,'.join(map(str, T)), end='°C\n')
print(f'Мінімальна температура: {min(T)} °C ', f'\nМаксимальна температура: {max(T)}°C', f'\nСередня температура: {sum(T) / len(T)}°C')