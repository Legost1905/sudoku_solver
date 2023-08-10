from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()  # создаем корневой объект - окно
root.title('Приложуха')  # заголовок окна
root.geometry('600x464+500+300')  # размеры окна
root.resizable(FALSE, FALSE)

font1 = font.Font(family='Colibry', size=20, weight='normal', slant='roman')
font2 = font.Font(family='Colibry', size=14, weight='normal', slant='roman')

size_big = 150
size_small = 50
sp_entry = []
sp_result = []

frame_main = Frame(width=454, height=454, borderwidth=2, relief=SOLID)
frame_main.place(x=5, y=5)

def create_frame_cube_1(frame, x_size, y_size):
    frame_cube = Frame(frame, width=x_size, height=y_size, borderwidth=1, relief=SOLID)
    return frame_cube

def create_frame_cube_2(frame, x_size, y_size):
    frame_cube = ttk.Frame(frame, width=x_size, height=y_size, borderwidth=6, relief=SOLID, padding=0)
    return frame_cube

def btn_command():
    for i in range(81):
        temp = sp_entry[i].get()
        if temp:
            sp_result.append(int(temp))
        else:
            sp_result.append(0)
    # print(sp_result)


for i in range(3):
    for j in range(3):
        frame_cube = create_frame_cube_1(frame_main, size_big, size_big)
        for k in range(3):
            for l in range(3):
                frame_sq = create_frame_cube_2(frame_cube, size_small, size_small)
                entry = Entry(frame_sq, font=font1, width=2, justify=CENTER)
                entry.pack()
                sp_entry.append(entry)
                # temp = entry.get()
                frame_sq.place(x=l * size_small, y=k * size_small)
        frame_cube.place(x=j * size_big, y=i * size_big)

btn_1 = Button(text='Получить \n решение', font=font2, command=btn_command)
btn_1.place(x=480, y=20)
btn_2 = Button(text='Очистить \n таблицу', font=font2, command=btn_command)
btn_2.place(x=480, y=100)

label_1 = Label(text='Сообщение:', font=font2)
label_1.place(x=475, y=180)
label_2 = Label(text='-', font=font2, width=10, justify=CENTER)
label_2.place(x=475, y=210)

root.mainloop()
