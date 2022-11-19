from tkinter import *
from tkinter.ttk import Combobox, Scrollbar
import os
w = 900
h = 480
window = Tk()
window.title("Телефонный справочник")
window.geometry(f"{w}x{h}")
window.config(bg="#c7fff8")
window.resizable(False, False)
logo = PhotoImage(file="Homework_9/Logo/PhoneBook.png")
window.iconphoto(False, logo)


screen = Listbox(window, width=50, height=10, font=(
    "Courier new", 14, "bold"), fg="#270bde", bd=1, bg="#6afceb")
screen.grid(row=4, column=1, rowspan=5, columnspan=3, padx=10)

scrollbar = Scrollbar(orient="vertical", command=screen.yview)
scrollbar.grid(row=4, column=3, columnspan=2, rowspan=4 ,sticky="sn")
screen["yscrollcommand"]=scrollbar.set

def open_all_file():
    global value_file
    with open(f"Homework_9/all_files.txt", encoding="UTF-8") as data:
        file_name = [i.strip().split(";") for i in data.readlines() if i != '']
    value_file = Combobox(window, width=20, values=[
                          i[0] for i in file_name], justify=CENTER)
    value_file.grid(row=1, column=2, sticky="wse", padx=10)
open_all_file()


Label(window, text="Номер:", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="e").grid(row=0, column=1, sticky="ne", pady=3, padx=10)
Label(window, text="Имя:", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="e").grid(row=0, column=1, sticky="se", padx=10)
Label(window, text="Комментарий:", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="e").grid(row=1, column=1, sticky="ne", padx=10)
Label(window, text="Выбор папки: ", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="w").grid(row=1, column=1, sticky="se", padx=10)
Label(window, text="Список контактов:", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="w").grid(row=3, column=1, sticky="wne", pady=7, padx=10)
Label(window, text="Имя новой папки: ", font=("Courier new", 14, "bold"),
      fg="#270bde", bg="#c7fff8", anchor="w").grid(row=2, column=2, sticky="swe", padx=10)


number = Entry(window, font=("Courier new", 14, "bold"),
               fg="#270bde", bd=1, bg="#6afceb")

name = Entry(window, font=("Courier new", 14, "bold"),
             fg="#270bde", bd=1, bg="#6afceb")

comment = Entry(window, font=("Courier new", 14, "bold"),
                fg="#270bde", bd=1, bg="#6afceb")

folder_name = Entry(window, font=("Courier new", 14, "bold"),
                    fg="#270bde", bd=5, bg="#6afceb")


number.grid(row=0, column=2, sticky="wen", pady=3, padx=10)
name.grid(row=0, column=2, sticky="wes", padx=10)
comment.grid(row=1, column=2, sticky="wen", pady=3, padx=10)
folder_name.grid(row=3, column=2, sticky="wne", padx=10)


text1 = ["Показать все контакты", "Открыть папку с контактами",
         "Добавить папку с контактами", "Удалить папку с контактами", "Добавить контакт", "Изменить контакт",
         "Удалить контакт", "Поиск по контактам"]


def read_file():
    with open(path, encoding="UTF-8") as data:
        contacts = [i.strip().split(";") for i in data.readlines()]
        [contacts.remove(i) for i in contacts if i[0] == '']
    return contacts


def get_contacts():
    try:
        list_contacts = [i[0] for i in read_file()]
        screen.delete(0, "end")
        for i in list_contacts:
            screen.insert("end", i)
    except:
        start = Label(window, height=3, relief=RIDGE, text="Пожалуйста,\nвыбирите и\nоткройте папку!",
                    font=("Courier new",14, "bold"), bg="#fc4242")
        start.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        start.after(900, lambda: start.destroy())


def open_file():
    global path
    file = value_file.get()
    path = "Homework_9/Phone_books/" + f"{file}"
    Label(window, text=f"Папка: {path[23:-4]}", font=("Courier new", 14, "bold"),
          fg="#270bde", bg="#c7fff8", anchor="w").grid(row=2, column=1, sticky="swe", padx=10)
    get_contacts()


def add_new_file():
    if len(folder_name.get()) == 0:
        lbl = Label(window, text="Введите название\nновой папки!",
                    relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242")
        lbl.grid(row=1, column=2, sticky="swe", rowspan=2, padx=10)
        lbl.after(800, lambda: lbl.destroy())
    else:
        with open("Homework_9/all_files.txt", "a", encoding="UTF-8") as data:
            data.write(folder_name.get() + ".txt\n")

        with open(f"Homework_9/Phone_books/{folder_name.get()}.txt", "w") as data:
            data.write("")
        open_all_file()
        folder_name.delete(0, "end")
        screen.delete(0, "end")

def del_file():
    if len(value_file.get()) == 0:
        lbl = Label(window, height=3, relief=RIDGE, text="Пожалуйста,\nвыбирите папку\nдля удаления!",
                    font=("Courier new",14, "bold"), bg="#fc4242")
        lbl.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        lbl.after(900, lambda: lbl.destroy())
    else:
        path = f"Homework_9/Phone_books/{value_file.get()}"
        os.remove(path)
        with open("Homework_9/all_files.txt", encoding="UTF-8") as data:
            books = [i.strip().split(";") for i in data.readlines()]
            [books.remove(i) for i in books if i[0] == '' or i[0] == value_file.get()]
        with open("Homework_9/all_files.txt", "w", encoding="UTF-8") as data:
            [data.write(i[0] + "\n") for i in books]
        open_all_file()
        screen.delete(0, "end")


def add_contact():
    try:
        if len(number.get()) == 0 or len(name.get()) == 0 or len(comment.get()) == 0:
            lbl = Label(window, height=4, text="Пожалуйста,\nзаполните поля\nполностью!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        elif not number.get().isdigit():
            lbl = Label(window, height=4, text="Номер\nсостоит только\nиз цифр!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        else:
            contact = ""
            contact += number.get() + " | " + name.get() + " - " + comment.get()
            with open(path, "a", encoding="UTF-8") as data:
                data.write('\n' + contact)
            number.delete(0, "end")
            name.delete(0, "end")
            comment.delete(0, "end")
            get_contacts()
    except:
        start = Label(window, height=3, relief=RIDGE, text="Пожалуйста,\nвыбирите и\nоткройте папку!", 
                        font=("Courier new", 14, "bold"), bg="#fc4242")
        start.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        start.after(900, lambda: start.destroy())


def del_cont():
    try:
        list_contacts = [i[0] for i in read_file()]
        id_contacts = screen.curselection()
        if len(id_contacts) == 0:
            lbl = Label(window, height=4, text="Пожалуйста\nвыберите контакт\nдля удаления!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        else:
            del list_contacts[id_contacts[0]]
            with open(path, "w", encoding="UTF-8") as data:
                [data.write(i + "\n") for i in list_contacts]
            get_contacts()
    except:
        start = Label(window, height=3, text="Пожалуйста,\nвыбирите и\nоткройте папку!", relief=RIDGE, 
                        font=("Courier new", 14, "bold"), bg="#fc4242")
        start.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        start.after(900, lambda: start.destroy())


def change_cont():
    try:
        list_contacts = [i[0] for i in read_file()]
        id_contacts = screen.curselection()
        if len(id_contacts) == 0:
            lbl = Label(window, height=4, text="Пожалуйста\nвыберите контакт\nдля изменения!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        elif not number.get().isdigit() and len(number.get()) > 0:
            lbl = Label(window, height=4, text="Номер\nсостоит только\nиз цифр!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        elif len(number.get()) == 0 or len(name.get()) == 0 or len(comment.get()) == 0:
            lbl = Label(window, height=4, text="Пожалуйста,\nзаполните поля\nполностью!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        else:
            list_contacts[id_contacts[0]] = number.get() + " | " + \
                name.get() + " - " + comment.get()
            with open(path, "w", encoding="UTF-8") as data:
                [data.write(i + "\n") for i in list_contacts]
            number.delete(0, "end")
            name.delete(0, "end")
            comment.delete(0, "end")
            get_contacts()
    except:
        start = Label(window, height=3, text="Пожалуйста,\nвыбирите и\nоткройте папку!", relief=RIDGE,
                        font=("Courier new",14, "bold"), bg="#fc4242")
        start.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        start.after(900, lambda: start.destroy())


def find_cont():
    try:
        screen.delete(0, END)
        list_contacts = [i[0] for i in read_file()]
        if not number.get().isdigit() and len(number.get()) > 0:
            lbl = Label(window, height=4, text="Номер\nсостоит только\nиз цифр!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen", rowspan=2, padx=10)
            lbl.after(800, lambda: lbl.destroy())
        elif len(number.get()) == 0 and len(name.get()) == 0 and len(comment.get()) == 0:
            lbl = Label(window, height=4, text="Пожалуйста,\nвведите номер, имя или\nкомментарий для поиска!",
                        relief=RIDGE, font=("Courier new", 14, "bold"), bg="#fc4242",)
            lbl.grid(row=0, column=1, sticky="wen",
                     rowspan=2, columnspan=2, padx=10)
            lbl.after(900, lambda: lbl.destroy())
        else:
            for i in list_contacts:
                if len(number.get()) > 0 and len(name.get()) > 0 and len(comment.get()) > 0:
                    if number.get().lower() in i.lower() and name.get().lower() in i.lower() and comment.get().lower() in i.lower():
                        screen.insert("end", i)
                        continue
                elif len(number.get()) > 0:
                    if number.get().lower() in i.lower():
                        screen.insert("end", i)
                        continue
                elif len(name.get()) > 0:
                    if name.get().lower() in i.lower():
                        screen.insert("end", i)
                        continue
                elif len(comment.get()) > 0:
                    if comment.get().lower() in i.lower():
                        screen.insert("end", i)
                        continue
            if screen.size() == 0:
                screen.insert("end", "Этот контакт в данной папке не найден,")
                screen.insert("end", "перейдите в другую папку.")
            number.delete(0, "end")
            name.delete(0, "end")
            comment.delete(0, "end")
    except:
        start = Label(window, height=3, text="Пожалуйста,\nвыбирите и\nоткройте папку!", relief=RIDGE,
                        font=("Courier new",14, "bold"), bg="#fc4242")
        start.grid(row=1, column=1, rowspan=2, sticky="nwe", padx=10)
        start.after(900, lambda: start.destroy())


Button(window, text=text1[0], command=get_contacts,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=0, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[1], command=open_file,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=1, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[2], command=add_new_file,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=2, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[3], command=del_file,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=3, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[4], command=add_contact,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=4, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[5], command=change_cont,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=5, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[6], command=del_cont,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=6, column=0, sticky="we", pady=11, padx=8)
Button(window, text=text1[7], command=find_cont,
       justify=LEFT, bd=1, font=("Courier new", 14, "bold"),
       fg="#270bde", bg="#6afceb").grid(row=7, column=0, sticky="we", pady=11, padx=8)
window.grid_columnconfigure(0, minsize=150)


window.mainloop()