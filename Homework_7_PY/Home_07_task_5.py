# Вводится натуральное число N.
# С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.
#
# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
#-------------

# size_matrix = int(input('Введите размер матрицы: '))
# matrix = [(1 if x == i else 0) for i in range(0, size_matrix) for x in range(0, size_matrix)]
# count = 1
# for i in matrix:
#     if count % size_matrix == 0:
#         print(i)
#     else:
#         print(i, end=" ")
#     count += 1
#----------------------------------
# Второй вариант
size_matrix = int(input('Введите размер матрицы: '))
print("----------------------------------------------------------------------------------")
matrix_2 = [[1 if x == i else 0 for i in range(size_matrix)] for x in range(size_matrix)]
for i in matrix_2:
    print(*i)