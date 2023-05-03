# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#    1 2 3 4 5
#    6
#    -> 5

n = int(input('Введите количество элементов массива: '))
Ai = input("Введите целые числа через пробел: ").split()
A= list(map(int, Ai))
if len(A) != n or n == 0:
    print('Введенные элементы не соответствуют количеству')
else:
    
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A[0])
    index = 0
    for i in range(1, n):
        count = abs(X - A[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A[index]} в массиве наиболее близко по величине к числу {X}')