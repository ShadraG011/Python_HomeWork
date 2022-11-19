import os
clear = lambda: os.system('cls')
clear()
import view, model


def start():
    while True:
        command = view.show_menu()
        match command:
            case 1:
                model.view_contacts()
            case 2:
                model.open_file()
                model.view_contacts()
            case 3:
                model.add_file(view.add_file())
                model.view_contacts()
            case 4:
                model.add_contact(view.write_new_contact())
                model.view_contacts()
            case 5:
                model.view_contacts()
                model.chan_cont(view.change_contact(), view.write_new_contact())
            case 6:
                model.view_contacts()
                model.del_cont(view.delete_contact())
            case 7: 
                model.find_cont(view.find_contact())
            case 0: 
                print("\nСпасибо, что выбрали наше приложение!\n")
                break


