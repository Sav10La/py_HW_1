# 2* Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите число х: '))
z = bool(input('Введите число z: '))
y = bool(input('Введите число y: '))

left = not (x or y or z)
right = not x and not y and not z
print(left == right)