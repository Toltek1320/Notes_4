from fileinput import filename 
import model
import view 

def start():
    view.greetings()

    while True:
        view.menu()
        answer = input()
               
        if answer == '1':
            notes = model.load_notes()
            model.display_notes(notes)
        elif answer == '2':
            model.add_note()             
        elif answer == '3':
             model.edit_note()
        elif answer == '4':
            model.delete_note()         
        elif answer == '5':
            search = input('Выберите как будем искать:\n'
                           '1. По дате\n'
                           '2. По ID\n ')
            if search == '1':          
                model.get_notes_by_date()
            else:
                model.get_note_by_id()
        elif answer == '6':
            break
        else:
            print("Неверная команда")
    
    print("Завершение работы")