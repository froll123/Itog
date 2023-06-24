import NOTE


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'текст должен быть больше {n} символов\n')
        text = input('введите тескт: ')
    else:
        return text

def create_note(number):
    title = check_len_text_input(
        input('введите название заметки: '), number)
    body = check_len_text_input(
        input('введите описание заметки: '), number)
    return NOTE.Note(title=title, body=body)


def menu():
    print("\nэто программа 'Заметки'. Имеются следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")

def goodbuy():
    print("Всго хорошего и отличного дня!")



