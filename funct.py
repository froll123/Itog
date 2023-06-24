import file_oper
import NOTE
import ui

number = 6  


def show(text):
    logic = True
    array = file_oper.read_file()
    if text == 'date':
        date = input('введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(NOTE.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + NOTE.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in NOTE.Note.get_date(notes):
                print(NOTE.Note.map_note(notes))
    if logic == True:
        print('нет ни одной заметки...')
        
        
def id_edit_del_show(text):
    id = input('введите id необходимой заметки: ')
    array = file_oper.read_file()
    logic = True
    for notes in array:
        if id == NOTE.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                NOTE.Note.set_title(notes, note.get_title())
                NOTE.Note.set_body(notes, note.get_body())
                NOTE.Note.set_date(notes)
                print('заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('заметка удалена...')
            if text == 'show':
                print(NOTE.Note.map_note(notes))
    if logic == True:
        print('такой заметки нет, вероятно, введен неверный id')
    file_oper.write_file(array, 'a')        
        
        

def add():
    note = ui.create_note(number)
    array = file_oper.read_file()
    for notes in array:
        if NOTE.Note.get_id(note) == NOTE.Note.get_id(notes):
            NOTE.Note.set_id(note)
    array.append(note)
    file_oper.write_file(array, 'a')
    print('добавлена новая заметка!')





