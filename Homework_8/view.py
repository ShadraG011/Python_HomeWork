text = "\nМеню:\n\
1. Показать все контакты\n\
2. Открыть файл с контактами\n\
3. Записать файл с контактами\n\
4. Добавить контакт\n\
5. Изменить контакт\n\
6. Удалить контакт\n\
7. Поиск по контактам\n\
0. Выход\n\
\nВведите команду: "

def show_menu():
        while True:
                try: 
                        a = int(input(text))
                        if a >= 0 and a <=7: return a
                        else: 
                                print("\n--------------------------------------------")
                                print("Ошибка выбора команды, попробуйте еще раз.")
                                print("--------------------------------------------")
                except: 
                        print("\n--------------------------------------------")
                        print("Ошибка выбора команды, попробуйте еще раз.")
                        print("--------------------------------------------")


def write_new_contact():
        while True:
                try: 
                        number = int(input("Введите номер: "))
                        name = input("Введите имя: ")
                        comment = input("Введите комментарий: ")
                        break
                except: 
                        print("Номер состоит только из цифр")
        
        return f"{number} | {name} - {comment}"


def change_contact():
        while True:
                name_or_num = input("\nВведите номер или имя контакта, которого вы хотите Изменить: ")
                if len(name_or_num) >= 3:
                        return name_or_num
                else: 
                        print("Введиет минимум 3 символа.")
                        continue

def delete_contact():
        while True:
                name_or_num = input("\nВведите номер или имя контакта, которого вы хотите Удалить: ")
                if len(name_or_num) >= 3:
                        return name_or_num
                else: 
                        print("Введиет минимум 3 символа.")
                        continue

def find_contact():
        while True:
                name_or_num = input("\nВведите номер или имя контакта, которого вы хотите Найти: ")
                if len(name_or_num) >= 3:
                        return name_or_num
                else: 
                        print("Введиет минимум 3 символа.")
                        continue

 
def add_file():
        name_file = input("Введите название папки: ")
        return name_file
