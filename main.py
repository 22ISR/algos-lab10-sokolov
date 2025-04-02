from tkinter import *

# окно
root = Tk()

# Функции приложения

# def on_button_click(value):
#     if value == "Добавить":

# Имя окна
root.title("Мой TODO-лист")

# разрешение окна
root.geometry("400x400")

# поле ввода
case = Entry().pack(anchor=N, padx=8, pady= 8)

# добавить
add_button = Button(text="Добавить")
add_button.pack()

# cписок элементов
listbox = Listbox(root, width=30, height=5)
listbox.pack(pady=10)

# выравнивание колонок

buttonFrame = Frame(root)
buttonFrame.pack(fill="none")

# создание колонки
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)

# удалить
delete_button = Button(buttonFrame,text="Удалить")
delete_button.grid(row=0, column=0, sticky="we")

# очистить всё
rab = Button(buttonFrame, text="Очистить всё") 
rab.grid(row=0, column=1, sticky="we")

# запуск приложения
root.mainloop()


