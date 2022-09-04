# 5 Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_number(input_text):
    while True:
        try:
            x1 = int(input("Введите x1: "))
            y1 = int(input("Введите y1: "))
            x2 = int(input("Введите x2: "))
            y2 = int(input("Введите y2: "))
        except ValueError:
            print("Это не целое число! Попробуйте снова.")     
            continue
        else:
            return x1, y1, x2, y2
            break

def distance(x1, y1, x2, y2):
    result = round(pow(pow((x2 - x1),2) + pow((y2 - y1),2), 0.5),2)
    print (result)

x1, y1, x2, y2 = input_number("Введите: ")
distance(x1, y1, x2, y2)