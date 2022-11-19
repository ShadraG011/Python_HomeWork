path = "Homework_8/Phone_books/phonebook.txt"
num = 1


def add_file(name_file: str):
    global path
    path = "Homework_8/Phone_books/"

    with open(f"Homework_8/all_files.txt", "a", encoding="UTF-8") as data:
        data.write(name_file + ".txt\n")

    with open(f"Homework_8/Phone_books/{name_file}.txt", "w", encoding="UTF-8") as data:
        data.write("")

    path += name_file + ".txt"


def open_file():
    global path

    with open(f"Homework_8/all_files.txt", encoding="UTF-8") as data:
        file_name = [i.strip().split(";") for i in data.readlines()]
    print("\n---------------------")
    print("Список папок:")
    [print(f"{i+1})", file_name[i][0][:-4]) for i in range(len(file_name))]
    print("---------------------")

    while True:
        try:
            num = int(input("Введие номер папки: "))
            break
        except:
            print("Ошибка ввода!")

    path = "Homework_8/Phone_books/"
    path += file_name[num-1][0]


def read_file():
    with open(path, encoding="UTF-8") as data:
        contacts = [i.strip().split(";") for i in data.readlines()]
        [contacts.remove(i) for i in contacts if i[0] == '']
    return contacts


def view_contacts():
    contacts = read_file()
    list = [i[0] for i in contacts]

    print("\n---------------------")
    print(f"Папка {path[23:-4]}")
    print("---------------------")

    print("\n---------------------")
    print(f"Список контактов:")
    [print(i) for i in list]
    print("---------------------")


def add_contact(contact: str):
    with open(path, "a", encoding="UTF-8") as data:
        data.write('\n' + contact)


def del_cont(name: str):
    bool = False
    contacts = read_file()
    list = [i[0] for i in contacts]

    for i in list:
        if name in i:
            list.remove(i)
            bool = True
    with open(path, "w", encoding="UTF-8") as data:
        [data.write(i + "\n") for i in list]

    if not bool:
        print("Такого контакта нет.")
    else:
        view_contacts()


def chan_cont(name: str, contact: str):
    bool = False
    contacts = read_file()
    list = [contacts[i][0] for i in range(len(contacts))]

    for i in range(len(list)):
        if name in list[i]:
            list[i] = contact
            bool = True
    with open(path, "w", encoding="UTF-8") as data:
        [data.write(i + "\n") for i in list]

    if not bool:
        print("Такого контакта нет.")
    else:
        view_contacts()


def find_cont(name: str):
    bool = False
    contacts = read_file()
    list = [contacts[i][0] for i in range(len(contacts))]

    print("\nПоиск по контактам:")
    for i in range(len(list)):
        if name in list[i]:
            print(list[i])
            bool = True

    if not bool:
        print("Ничего не найдено.\n")
    else:
        print()
