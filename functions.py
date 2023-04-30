import file_operations
import Note
import menu

def add():
    note = menu.create_note()
    array = file_operations.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operations.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = file_operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате день/месяц/год: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Заметок нет')


def edit_or_del(text):
    id = input('Введите id заметки: ')
    array = file_operations.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = menu.create_note()
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такая заметка отсутствует')
    file_operations.write_file(array, 'a')