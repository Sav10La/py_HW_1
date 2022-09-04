# 3 Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1    
# - x=-34; y=-30 -> 3

def input_number(input_text):
    while True:
        x = input("Введите x: ")
        y = input("Введите y: ")
        try:
            val_x = int(x)
            val_y = int(y)
            if val_x == 0 or val_y == 0:  # if equals zero
                print("Введеное число не может быть нулем, попробуйте снова")
                continue
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good, val is >=  0 and an integer
    return val_x, val_y

def check_coordinates(x, y):
    if x > 0 and y > 0:
        print('1 четверть')
    elif x < 0 and y > 0:
        print('2 четверть')
    elif x < 0 and y < 0:
        print('3 четверть')
    else:
        print('4 четверть')

x, y = input_number('Введите числа: ')
check_coordinates(x, y)