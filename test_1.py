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
#
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
#
#

from tkinter import *
from tkinter import ttk
import re

# root.resizable(False, True)     # запрет изменять размеры окна по ширине и высоте
# root.minsize(200, 250)  # минимальные размеры окна
# root.maxsize(500, 550)  # максимальные размеры окна

# root.attributes('-fullscreen', True)      # полный экран
# root.attributes('-alpha', 1.0)      # прозрачность окна
# root.attributes('-toolwindow', True)    # отсутствие верхней панели окна

root = Tk()  # создаем корневой объект - окно
root.title('Приложуха')  # заголовок окна
root.geometry('400x350+500+300')  # размеры окна

# блок функций

def btn_command():
    pass

def is_valid(temp, op):
    result = re.match("^\d{0,1}$", temp) is not None
    return result

def entry_unfocus(event):
    result = entry.get()
    if str(result) != '0' or not result:
        label_2['text'] = result
        label_1.focus()
    else:
        entry.delete(0, END)
        entry.focus()


def entry_focus(event):
    entry.delete(0, END)

check = (root.register(is_valid), '%P', '%V')

errmsg = StringVar()


label_1 = ttk.Label()
label_1.config(text='1 Label', font=14)
label_1.place(x=50, y=30)

label_2 = ttk.Label()
label_2.config(text='2 Label', font=14)
label_2.place(x=280, y=30)

entry = ttk.Entry()
entry.insert(0,  'i')
entry.config(font=14, width=3, justify='center')
entry.config(validate='key', validatecommand=check)
entry.place(x=65, y=130)
entry.bind('<FocusIn>', entry_focus)
entry.bind('<FocusOut>', entry_unfocus)



btn = ttk.Button()
btn.config(text='Unfocus', command=btn_command)
btn.place(x=280, y=130)

def finish():
    root.destroy()
    print('Окно успешно закрылось')  # сообщение, отправляемое в консоль при закрытии окна


root.protocol('WM_DELETE_WINDOW', finish)
root.mainloop()
