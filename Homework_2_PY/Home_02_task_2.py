# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# ----------------------------------------------

#Сначала проверка (нахождение суммы и произведения одних и тех же чисел)
from random import randint

# print("Введите натуральные числа X и Y: ")
# X = 2#randint (0, 1000)
# Y = 2#randint (0, 1000)
# print(f"X= {X}, Y= {Y}")
# S = X + Y
# P = X * Y
# print(f"Сумма чисел= {S}, Произведение чисел= {P}")
#------------------------------------------------

# Поиск X и Y
import math

S = int(input("Введите сумму: "))
P = int(input("Введите произведение: "))

X = (S + math.sqrt(S ** 2 - 4 * P)) / 2
Y = S - X

if S == X + Y and P == X * Y:
    print(f"Число Х= {round(X)}, Число Y= {round(Y)}")
else:
    print(("Неверно подобрано значение суммы!"))


