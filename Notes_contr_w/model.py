import datetime
import json

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Заметка: {note['body']}")
        print(f"Дата и время: {note['timestamp']}")
        print('+++++++++++++++++')

def add_note():
    notes = load_notes()
    id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

def get_notes_by_date():
    notes = load_notes()
    date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date)]
    if filtered_notes:
        display_notes(filtered_notes)
    else:
        print("Заметок на указанную дату не найдено")

def get_note_by_id():
    notes = load_notes()
    id = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        print("Заметка найдена:")
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Заметка: {note['body']}")
        print(f"Дата и время: {note['timestamp']}")
    else:
        print("Заметка с указанным ID не найдена")

def edit_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        print("Редактирование заметки:")
        print(f"Старый заголовок: {note['title']}")
        new_title = input("Введите новый заголовок заметки: ")
        print(f"Старая заметка: {note['body']}")
        new_body = input("Введите новую заметку: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note['title'] = new_title
        note['body'] = new_body
        note['timestamp'] = timestamp

        save_notes(notes)
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с указанным ID не найдена")

def delete_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для удаления: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка успешно удалена!")
    else:
        print("Заметка с указанным ID не найдена")