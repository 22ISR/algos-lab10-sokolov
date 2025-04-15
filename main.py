from tkinter import *

# окно
root = Tk()

# Функции приложения

def on_button_click(value):
    selected = listbox.curselection()
    if value == "Добавить":
        The_finished_text = case.get()  # Получаем текст из поля ввода
        listbox.insert(listbox.index("end"), The_finished_text)

    elif value == "Удалить":
        selected == "Удалить"
        listbox.delete(selected[0])

    elif value == "Очистить всё":
        listbox.delete(0,listbox.index("end"))
        

# Имя окна
root.title("Мой TODO-лист")

# разрешение окна
root.geometry("400x400")

# поле ввода
case = Entry()
case.pack(anchor=N, padx=8, pady= 8)

# добавить
add_button = Button(root,text="Добавить", command=lambda value ="Добавить": on_button_click(value))
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
delete_button = Button(buttonFrame,text="Удалить", command=lambda value="Удалить": on_button_click(value))
delete_button.grid(row=0, column=0, sticky="we")

# очистить всё
rab = Button(buttonFrame, text="Очистить всё", command=lambda value="Очистить всё": on_button_click(value)) 
rab.grid(row=0, column=1, sticky="we")

# запуск приложения
root.mainloop()

