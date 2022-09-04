# 4 Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

def input_number(input_text):
    while True:
        number = input("Введите четверть: ")
        try:
            val = int(number)
            if val < 1 or val > 4 :  # if not a positive int print message and ask for input again
                print("Нужно ввести число от 1 до 4, попробуйте снова")
                continue
            break
        except ValueError:
            print("Это не целое число!")
        # else all is good, val is within range and an integer
    return val

def check_quarter(number):
    if quarter == 1:
        result = "x = (0, +∞); y = (0, +∞)"
    elif quarter == 2:
        result = "x = (0, -∞); y = (0, +∞)"
    elif quarter == 3:
        result = "x = (0, -∞); y = (0, -∞)"
    elif quarter == 4:
        result = "x = (0, +∞); y = (0, -∞)"
    print (result)

quarter = input_number("Введите четверть: ")
check_quarter(quarter)