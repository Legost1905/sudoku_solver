from tkinter import *
from tkinter import ttk
from tkinter import font
from module_1 import solve_matrix, squadrone_matrix, print_check_matr, create_matrix_working
import re

# создаем само окно, указываем название и размеры окна
root = Tk()
root.title('Решатель судоку')
root.geometry('600x464+500+300')
root.resizable(FALSE, FALSE)

# указываем используемые шрифты
font1 = font.Font(family='Colibry', size=20, weight='normal', slant='roman')
font2 = font.Font(family='Colibry', size=14, weight='normal', slant='roman')
# используемые размеры для внутренних окон
size_big = 150
size_small = 50

# задаем массив входных данных таблицы
sp_entry = []

# внешняя рамка судоку-таблицы
frame_main = Frame(width=454, height=454, borderwidth=2, relief=SOLID)
frame_main.place(x=5, y=5)

class FrameCube():
    sp_entry = []


    pass

def create_frame_cube_1(frame, x_size, y_size):     # создание Frame 1 стиля
    frame_cube = Frame(frame, width=x_size, height=y_size, borderwidth=1, relief=SOLID)
    return frame_cube


def create_frame_cube_2(frame, x_size, y_size):     # создание Frame 2 стиля
    frame_cube = ttk.Frame(frame, width=x_size, height=y_size, borderwidth=6, relief=SOLID, padding=0)
    return frame_cube


def is_valid(temp, op):     # проверка на валидность входного значения
    result = re.match("^\d{0,1}$", temp) is not None
    return result


# def entry_unfocus(event):
#     result = entry.get()
#     if str(result) == '0':
#         entry.delete(0, END)
#         entry.focus()
# entry.bind('<FocusOut>', entry_unfocus)

def create_matrix_from_sp(sp):    # создание матрицы 9х9 из массива в 81 элемент
    # задаем счетчики для строки и столбца матрицы
    # идем по массиву и заполняем матрицу
    # на выходе квадрируем матрицу

    new_sp = [[0 for _ in range(9)] for _ in range(9)]
    counter_j = 0
    counter_i = 0
    for elem in sp:
        if counter_j == 9:
            counter_j = 0
            counter_i += 1
        new_sp[counter_i][counter_j] = elem
        counter_j += 1
    return new_sp


def create_sp_from_matrix(sp):      # создание массива в 81 элемент из матрицы 9х9
    new_sp = []
    for i in range(9):
        for j in range(9):
            new_sp.append(sp[i][j])
    return new_sp


def matrix_entry_input(sp):     # считывание полей Entry
    # на входе имеем массив полей Entry
    # если поле Entry не пустое, считываем значение
    # иначе присваиваем 0
    # на выходе преобразовываем массив в матрицу

    sp_exit = []
    for i in range(81):
        temp = sp[i].get()
        if temp:
            sp_exit.append(int(temp))
        else:
            sp_exit.append(0)
    return create_matrix_from_sp(sp_exit)


def matrix_entry_output(sp):    # заполнение полей Entry
    # функция работает с глобальным массивом полей Entry

    for i in range(81):
        temp = sp_entry[i].get()
        if not temp:
            sp_entry[i].insert(0, str(sp[i]))
        else:
            sp_entry[i].config(state='disabled')

def btn_command_1():    # получить решение судоку
    # получаем матрицу входных значений и квадрируем ее
    # получаем решение судоку-таблицы
    # квадрируем решение и получаем список для массива Entry
    # заполняем поля Entry

    matrix_result = squadrone_matrix(matrix_entry_input(sp_entry))
    matrix = solve_matrix(matrix_result)
    sp_result = create_sp_from_matrix(squadrone_matrix(matrix))
    matrix_entry_output(sp_result)


def btn_command_2():    # очистить поле таблицы
    # очищаем поля Entry
    # делаем все поля Entry активными
    # возвращаем фокус на 1-ю ячейку таблицы

    for i in range(81):
        sp_entry[i].delete(0, END)
        sp_entry[i].config(state='normal')
    sp_entry[0].focus()
    pass


check = (root.register(is_valid), '%P', '%V')

for i in range(3):
    for j in range(3):
        frame_cube = create_frame_cube_1(frame_main, size_big, size_big)
        for k in range(3):
            for l in range(3):
                frame_sq = create_frame_cube_2(frame_cube, size_small, size_small)
                entry = Entry(frame_sq, font=font1, width=2, justify=CENTER)
                entry.config(validate='key', validatecommand=check)
                entry.pack()
                sp_entry.append(entry)
                frame_sq.place(x=l * size_small, y=k * size_small)
        frame_cube.place(x=j * size_big, y=i * size_big)

btn_1 = Button(text='Получить \n решение', font=font2, command=btn_command_1)
btn_1.place(x=480, y=20)
btn_2 = Button(text='Очистить \n таблицу', font=font2, command=btn_command_2)
btn_2.place(x=480, y=100)

label_1 = Label(text='Сообщение:', font=font2)
label_1.place(x=475, y=180)
label_2 = Label(text='-', font=font2, width=10, justify=CENTER)
label_2.place(x=475, y=210)

root.mainloop()
