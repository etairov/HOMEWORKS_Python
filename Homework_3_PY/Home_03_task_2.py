# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
# 1 2 3 4 5
# 6 -> 5
# --------------

from random import randint

n = randint(5, 15)
list = [randint(0, n) for i in range(n)]
print(list)
diff = 0
X = int(input('Введите X: '))
#----------------------------------
# Мое решение. Пока не получилось сопоставить значения списков list и list_diff
# list_diff = []
# for i in range(n):
#     diff = X - list[i]
#     list_diff.append(diff)
# min = abs(list_diff[0])
# for j in range(n):
#     if abs(list_diff[j]) < min:
#         min = abs(list_diff[j])
# print(list_diff)
# print(min)
# print(f'Ближайшее к {X} число --> {}')

#--------------------------------------------
# Вариант решения с ГитХаб

min = abs(X - list[0])
j = 0
for i in range(1, n):
    count = abs(X - list[i])
    if count < min:
        min = count
        j = i
print(f'Число {list[j]} ,ближайшее к числу {X}, их разница {abs(X - list[j])}')

#---------------------------------------------------------------------------
# Короткое решение через lambda

# print(f'Ближайшее к {X} число --> {min(list, key = lambda x: abs(x-X))}')

