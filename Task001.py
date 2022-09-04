# 1 Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_number(input_text):
    while True:
        number = input("Введите число: ")
        try:
            val = int(number)
            if val < 1 or val > 7:  # if not a positive int print message and ask for input again
                print("Нужно ввести число от 1 до 7, попробуйте снова")
                continue
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good, val is >=  0 and an integer
    return val

def check_day(day):
    if 5 < day < 8:
        print('Выходной')
    elif 0 < day < 6:
        print('Не выходной')


day = input_number('Введите число: ')
check_day(day)