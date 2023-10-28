class Cube:

    pass


def create_matrix_working(matrix):  # создание матрицы со списками вместо пустых клеток
    # на входе имеем список девяти списков
    # вместо пропущенного числа стоит 0
    # в новом списке вместо 0 ставится список с числами от 1 до 9
    # на выходе получаем матрицу, где вместо пустого элемента список с возможными числами

    matrix_working = [[0 for j in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                matrix_working[i][j] = [k + 1 for k in range(9)]
            else:
                matrix_working[i][j] = matrix[i][j]
    return matrix_working


def print_matr(matrix):  # вывод матрицы со списками при наличии
    for i in matrix:
        for j in i:
            print(str(j).ljust(2), end=' ')
        print()
    print()


def print_check_matr(matrix):  # вывод матрицы с прочерком вместо списка
    for i in matrix:
        for j in i:
            if isinstance(j, list) or j == 0:
                print('_ ', end=' ')
            else:
                print(str(j).ljust(2), end=' ')
        print()
    print()


def check_line(matrix_row):  # исключение повторяющихся значений в списках в строке
    # перебираем значения строки (списка)
    # если элемент строки не число, а список, то заходим новым циклом в эту строку
    # исключаем из найденного списка все целые значения строки
    # на выходе получаем строку, где в списках исключены значения целых чисел этой строки

    for i in range(len(matrix_row)):
        if isinstance(matrix_row[i], list):
            for j in matrix_row:
                if j in matrix_row[i] and isinstance(j, int):
                    matrix_row[i][j - 1] = 0
    return matrix_row


def check_row_matrix(matrix):  # проверка матрицы по строкам
    # проверяем каждую строку матрицы методом check_line

    for i in range(9):
        matrix[i] = check_line(matrix[i])
    return matrix


def transpose_matrix(matrix):  # транспонирование матрицы
    new_matrix = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def check_column_matrix(matrix):  # проверка матрицы по столбцам
    # транспонируем матрицу, проверяем каждую строку матрицы методом check_line
    # транспонируем обратно исправленную матрицу

    new_matrix = check_row_matrix(transpose_matrix(matrix))
    return transpose_matrix(new_matrix)


def squadrone_matrix(matrix):  # "квадратирование" матрицы (каждая строка - блок 3х3)
    new_matrix = [[] for _ in range(9)]
    new_matrix[0] = matrix[0][0:3] + matrix[1][0:3] + matrix[2][0:3]
    new_matrix[1] = matrix[0][3:6] + matrix[1][3:6] + matrix[2][3:6]
    new_matrix[2] = matrix[0][6:9] + matrix[1][6:9] + matrix[2][6:9]
    new_matrix[3] = matrix[3][0:3] + matrix[4][0:3] + matrix[5][0:3]
    new_matrix[4] = matrix[3][3:6] + matrix[4][3:6] + matrix[5][3:6]
    new_matrix[5] = matrix[3][6:9] + matrix[4][6:9] + matrix[5][6:9]
    new_matrix[6] = matrix[6][0:3] + matrix[7][0:3] + matrix[8][0:3]
    new_matrix[7] = matrix[6][3:6] + matrix[7][3:6] + matrix[8][3:6]
    new_matrix[8] = matrix[6][6:9] + matrix[7][6:9] + matrix[8][6:9]
    return new_matrix


def check_square_matrix(matrix):  # проверка матрицы по квадратам
    # квадратируем матрицу, проверяем каждую строку матрицы методом check_line
    # квадратируем матрицу обратно

    new_matrix = check_row_matrix(squadrone_matrix(matrix))
    return squadrone_matrix(new_matrix)


def list_count(matrix_element):  # подсчет ненулевых значений в списке
    total = 0
    for i in matrix_element:
        if i != 0:
            total += 1
    return total


def check_matrix(matrix):  # проверка матрицы и замена пустых списков на число
    # проверяем матрицу по строкам, столбцам, блокам (квадратам)
    # при проверке исключаем из встречающихся списков повторяющиеся значения
    # если в каком-то списке всего 1 значение, то в нем конечное число
    # заменяем этот список на полученное число

    matrix = check_square_matrix(check_column_matrix(check_row_matrix(matrix)))
    for i in range(9):
        for j in range(9):
            if isinstance(matrix[i][j], list):
                if list_count(matrix[i][j]) == 1:
                    matrix[i][j] = sum(matrix[i][j])
    return matrix


def check_list_in_matrix(matrix):  # проверка наличия в матрице списка
    for i in matrix:
        for j in i:
            if isinstance(j, list):
                return True
    return False


def filling_matrix(matrix):  # получение заполненной матрицы
    # пока в матрице есть хотя бы один список, проходим по нему

    flag = True
    while flag:
        matrix = check_matrix(matrix)
        flag = check_list_in_matrix(matrix)
    return matrix


def solve_matrix(matrix):  # получение решения судоку
    # передаю исходную матрицу с нулями вместо пустых значений

    return filling_matrix(create_matrix_working(matrix))
