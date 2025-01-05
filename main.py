# import numpy as np
import requests 

from matrix_run import *


# получение матрицы из заданного url и обход в заданном направлении
def get_matrix(url: str, direction: str) -> list[int]:
    response = requests.get(url)
    # функция возвращает получившийся список и заданную матрицу в исходном виде
    return matrix_run(matrix_from_text(response.text), direction), response.text


SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

result_list, source_matrix = get_matrix(SOURCE_URL, 'L')
print("Результат обхода матрицы против часовой стрелки:")
list_print(result_list)
print('\n')
print(source_matrix)

result_list, source_matrix = get_matrix(SOURCE_URL, 'R')
print("Результат обхода матрицы по часовой стрелке:")
list_print(result_list)
print('\n')
print(source_matrix)
