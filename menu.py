import Note

def create_note():
    title = input('Введите название заметки: ')
    body = input('Введите текст заметки: ')
    return Note.Note(title=title, body=body)

def menu():
    print("\n1 - добавить заметку\
           \n2 - список всех заметок\
           \n3 - редактировать заметку\
           \n4 - удалить заметку\
           \n5 - фильтрация заметок по дате\
           \n6 - показать заметку по идентификатору\
           \n7 - выход")