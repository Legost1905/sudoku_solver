# import tkinter
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
#
# window = Tk()
# window.title('Судоку')
# window.geometry('350x300')
#
# frame = Frame(window, borderwidth=1, highlightcolor='black')
# frame.pack(padx=10, pady=10)
#
# table = Grid(frame)
# table.pack()
#
# # for i in range(9): window.columnconfigure(index=i, weight=1)
# # for i in range(9): window.rowconfigure(index=i, weight=1)
#
# for i in range(9):
#     for j in range(9):
#         btn = ttk.Entry(text=f'{i} {j}')
#         btn.grid(row=i, column=j, padx=2, pady=2, ipadx=5, ipady=5)
#
#
#
# window.mainloop()


#
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# # Создание рамки
# frame = tk.Frame(root, borderwidth=1, highlightbackground="black")
# frame.pack(padx=20, pady=20)
#
# # Создание таблицы внутри рамки
# table = ttk.Treeview(frame)
# table.pack()
#
# # Добавление столбцов
# table["columns"] = ("1", "2", "3")
#
# # Установка ширины столбцов
# table.column("#0", width=50, minwidth=50)
# table.column("1", width=100, minwidth=50)
# table.column("2", width=100, minwidth=50)
# table.column("3", width=100, minwidth=50)
#
# # Установка заголовков столбцов
# table.heading("#0", text="Column 1")
# table.heading("1", text="Column 2")
# table.heading("2", text="Column 3")
# table.heading("3", text="Column 4")
#
# # Добавление элементов в таблицу
# for i in range(3):
#     table.insert("", index=i, values=("Value 1", "Value 2", "Value 3"))
#
# root.mainloop()


# matrix_input = [[0 for j in range(9)] for _ in range(9)]

# matrix_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
import os

matrix_input = [[0, 6, 0, 3, 0, 8, 0, 0, 0],
                [3, 0, 4, 5, 6, 0, 0, 0, 0],
                [0, 8, 0, 4, 0, 9, 7, 3, 0],
                [4, 9, 6, 0, 0, 2, 1, 0, 5],
                [0, 1, 0, 0, 4, 5, 0, 0, 9],
                [7, 5, 0, 0, 9, 0, 0, 0, 8],
                [0, 0, 0, 6, 0, 3, 5, 0, 0],
                [0, 0, 9, 0, 5, 7, 8, 0, 3],
                [5, 3, 0, 0, 8, 0, 6, 0, 0]]

matrix_working = [[0 for j in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if matrix_input[i][j] == 0:
            matrix_working[i][j] = [k + 1 for k in range(9)]
        else:
            matrix_working[i][j] = matrix_input[i][j]


def print_matr(matrix):  # вывод матрицы со списками при наличии
    for i in matrix:
        for j in i:
            print(str(j).ljust(2), end=' ')
        print()
    print()


def print_chek_matr(matrix):  # вывод матрицы с прочерком вместо списка
    for i in matrix:
        for j in i:
            if isinstance(j, list) or j == 0:
                print('_ ', end=' ')
            else:
                print(str(j).ljust(2), end=' ')
        print()
    print()


def check_line(matrix_row):  # исключение повторяющихся значений в списках в строке
    for i in range(len(matrix_row)):  # идем по строке значений
        if isinstance(matrix_row[i], list):  # если элемент строки список
            for j in matrix_row:  # идем по строке новым циклом
                if j in matrix_row[i] and isinstance(j, int):  # если элемент есть в найденном списке
                    matrix_row[i][j - 1] = 0  # редактируем список
    return matrix_row  # из каждого списка строки исключены целые символы строки


def check_row_matrix(matrix):  # проверка матрицы по строкам
    for i in range(9):
        matrix[i] = check_line(matrix[i])  # проверяем каждую строку
    return matrix


def transpose_matrix(matrix):  # транспонирование матрицы
    new_matrix = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def check_column_matrix(matrix):  # проверка матрицы по столбцам
    new_matrix = check_row_matrix(transpose_matrix(matrix))  # транспонируем матрицу, проверяем ее по строкам
    return transpose_matrix(new_matrix)  # транспонируем обратно исправленную матрицу


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
    new_matrix = check_row_matrix(squadrone_matrix(matrix))
    last_matrix = squadrone_matrix(new_matrix)
    return last_matrix


def list_count(matrix_element):  # подсчет ненулевых значений в списке
    total = 0
    for i in matrix_element:
        if i != 0:
            total += 1
    return total


def check_matrix(matrix):  # проверка матрицы и замена пустых списков на число
    # matrix = check_row_matrix(matrix)
    # print_chek_matr(matrix)
    # matrix = check_column_matrix(matrix)
    # print_chek_matr(matrix)
    # matrix = check_square_matrix(matrix)
    # print_chek_matr(matrix)
    matrix = check_square_matrix(check_column_matrix(check_row_matrix(matrix)))

    # полученная выше матрица имеет списки
    # если в каком-то списке всего 1 значение, то в нем конечное число
    # заменяем этот список на полученное число

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
    flag = True
    while flag:  # пока в матрице есть хотя бы один список, проходим по нему
        matrix = check_matrix(matrix)
        flag = check_list_in_matrix(matrix)
    return matrix


print_chek_matr(matrix_input)
matrix_working = filling_matrix(matrix_working)
print_matr(matrix_working)

#os.system('PAUSE')