import sqlite3
connect = sqlite3.connect('notes.db')
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
               id INTEGER PRIMARY KEY
               AUTOINCREMENT,
            title TEXT,
            content TEXT,
            date TIMESTAMP
)
""")

connect.commit()


def add_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    date = input("Введите дата и время создание заметки: ")
    
    cursor.execute("""
    INSERT INTO notes (title, content, date) VALUES (?, ?, ?) """, (title, content, date))

    connect.commit()
    print("Заметка успешно добавлено! ")

def view_note():

    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    if notes:
        print("\n Список всех заметок: ")
        for note in notes:
            print(f"ID: {note[0]}, Заголок: {note[1]}, Дата создание: {note[2]}")
        else:
            print("Нет заметок для отображения.")
    connect.commit()

def edit_note():
    note_id = int(input("Введите ID заметку которую хотите отредактировать: "))

    cursor.execute('SELECT id, title, date FROM notes')
    notes = cursor.fetchone()

    if notes:
        new_title = input(f" Текущий заголовок: {notes[1]}\nВведите новый заголовок")
        new_content = input(f" Текущее содержание: {notes[1]}\nВведите новое содержание")

        cursor.execute("UPDATE notes SET title = ?, content = ?, WHERE id = ?", (new_title, new_content, note_id))
        connect.commit()
    else:
        print("Нет заметок.")

def delete_note():
    note_id = int(input("Введите ID  которую хотите удалить: "))

    cursor.execute("DELETE FROM notes WHERE id=?")

    if cursor.rowcount > 0:
        print("Заметка удалена!")
    else:
        print("Заметка с таким ID не найдено")

        connect.close()

def menu():

    while True:
        print("\n1. Добавить заметку")
        print("2. Посмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие от 1 до 5: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
            print("Выход...") 
        else:
            print("Неверный выбор попробуйте снова")

         
menu()
    


            



    







