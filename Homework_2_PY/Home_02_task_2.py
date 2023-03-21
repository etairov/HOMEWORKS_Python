# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# ----------------------------------------------

#Сначала проверка (нахождение суммы и произведения одних и тех же чисел)
from random import randint

print("Введите натуральные числа X и Y: ")
X = randint (0, 1000)
Y = randint (0, 1000)
print(f"X= {X}, Y= {Y}")
S = X + Y
P = X * Y
print(f"Сумма чисел= {S}, Произведение чисел= {P}")
#------------------------------------------------

# Поиск X и Y
S = int(input("Введите сумму: "))
#P = int(input("Введите произведение: "))
X = S - Y
Y = S - X
if S == X + Y and P == X * Y:
    print(f"Число Х= {X}, Число Y= {Y}")
else:
    print(("Неверно подобрано значение суммы!"))