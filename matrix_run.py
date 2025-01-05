import numpy as np
# Обход матрицы по спирали
# direction='L' - против часовой стрелки
# direction='R' - по часовой стрелке

def matrix_run(matrix, direction='L'):
    bottom_row = matrix.shape[0] - 1
    right_column = matrix.shape[1] - 1
    result = []
    # начальные значения для направления обхода
    if direction == 'L':        # начинаем двигаться вниз снаружи матрицы
        top_row = -1            # начальная позиция сверху матрицы
        left_column = 0
        i = -1
        j = 0
        step_i = 1
        step_j = 0
    else:                       # начинаем двигаться вправо снаружи матрицы
        top_row = 0
        left_column = -1        # начальная позиция слева от матрицы
        i = 0
        j = -1
        step_i = 0
        step_j = 1

    num = 0
    limit = (bottom_row + 1) * (right_column + 1)   # количество элементов матрицы

    while True:
        num += 1
        if num > limit:
            break

        # текущий элемент матрицы -> список
        i += step_i
        j += step_j
        result.append(matrix[i, j])

        if i == bottom_row and j == left_column:    # нижний левый угол оставшейся части матрицы
            if direction == 'L':    # дальнейшее напрвление обхода - вправо, верхнюю границу обхода сдвинуть вниз
                top_row += 1        
                step_i = 0
                step_j = 1
            else:                   # дальнейшее напрвление обхода - вверх, правую границу обхода сдвинуть влево
                right_column -= 1
                step_i = -1
                step_j = 0

        elif i == bottom_row and j == right_column:    # нижний правый угол оставшейся части матрицы
            if direction == 'L':    # # дальнейшее напрвление обхода - вверх, левую границу обхода сдвинуть вправо
                left_column += 1
                step_i = -1
                step_j = 0
            else:                   # # дальнейшее напрвление обхода - влево, верхнюю границу обхода сдвинуть вниз
                top_row += 1
                step_i = 0
                step_j = -1
        elif i == top_row and j == right_column:    # верхний правый угол оставшейся части матрицы
            if direction == 'L':    # # дальнейшее напрвление обхода - влево, нижнюю границу обхода сдвинуть вверх
                bottom_row -= 1
                step_i = 0
                step_j = -1
            else:                   # # дальнейшее напрвление обхода - вниз, левую границу обхода сдвинуть вправо
                left_column += 1
                step_i = 1
                step_j = 0
        elif i == top_row and j == left_column and (left_column > 0 or top_row > 0):    # верхний левый угол оставшейся части матрицы
            if direction == 'L':    # # дальнейшее напрвление обхода - вниз, правую границу обхода сдвинуть влево
                right_column -= 1
                step_i = 1
                step_j = 0
            else:                   # # дальнейшее напрвление обхода - вправо, нижнюю границу обхода сдвинуть вверх
                bottom_row -= 1
                step_i = 0
                step_j = 1

    return result


# Печать списка
def list_print(list_in):
    for list_member in list_in:
        print(list_member, end=' ')

    print('')
    return True


# Получение квадратной матрицы из текста вида:
"""
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
def matrix_from_text(matrix_txt):
    # Удаление всех символов, кроме цифр и прбелов
    matrix_string = matrix_txt.replace('+', "").replace('-', "").replace('|', "").replace('\n\n', "").split()
    # список чисел, разделенных пробелами
    matrix_list = [int(z) for z in matrix_string]
    # размерность квадратной матрицы N
    matrix_dimension = int(len(matrix_list) ** 0.5)
    # функция возвращает двумерный массив N x N
    return np.array(matrix_list).reshape(matrix_dimension, matrix_dimension)
