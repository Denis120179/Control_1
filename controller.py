import functions as f
import menu


def run():
    user_choice = ''
    while user_choice != '7':
        menu.menu()
        user_choice = input().strip()
        if user_choice == '1':
            f.add()            
        if user_choice == '2':
            f.show('all')
        if user_choice == '3':
            f.show('all')
            f.edit_or_del('edit')            
        if user_choice == '4':
            f.show('all')
            f.edit_or_del('del')            
        if user_choice == '5':
            f.show('date')
        if user_choice == '6':
            f.show('id')
            f.edit_or_del('show')
        if user_choice == '7':            
            break