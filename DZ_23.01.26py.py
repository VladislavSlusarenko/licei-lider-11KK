from os import system
from math import sqrt, pi

def inputPositive(S) -> float:
    while True:
        try:
            i = float(input(S))
            if i <= 0:
                print('Значення повинно бути додатнім числом! Спробуйте ще раз.')
            else:
                return i
        except ValueError:
            print('Помилка вводу! Спробуйте ще раз.')

def box_side(diameter):
    # квадрат вписаний у коло: діагональ = діаметр диска
    return diameter / sqrt(2)

def heat_quantity(m, c, t1, t2):
    return m * c * (t2 - t1)

system('cls')

# Завдання 1. Подарункова коробка
disk_diameter = inputPositive('Введіть діаметр диска (мм): ')
side = box_side(disk_diameter)
print('Сторона подарункової коробки =', round(side, 2), 'мм')

# Завдання 2. Кількість теплоти
m = 5       # кг
t1 = 20     # °С
t2 = 100    # °С
c = 2000    # Дж/°С

Q = heat_quantity(m, c, t1, t2)
print('Кількість теплоти, необхідна для нагрівання =', Q, 'Дж')
