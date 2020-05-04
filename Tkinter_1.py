import tkinter
#import b as b

# Описываю какие-то события


def handler1(event):
    print('Hello World! x =', event.x, 'y =', event.y)

def handler2(event):
    exit()

# Инициализация
root = tkinter.Tk()

hello_label = tkinter.Label(root, text='Hello world!', font="Times 40")
hello_label.pack()


# Привязка обработчиков - к событию и виджету:
# виджет.bind(событие, обработчик) bind - привязать
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)


# Главный проект
root.mainloop()

