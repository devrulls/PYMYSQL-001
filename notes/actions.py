import notes.note as model


class Actions:

    def create(self, user):
        print(f"\nok {user[1]}!!, let's create a note..")

        title = input("Enter the title of the note: ")
        description = input("Enter the description of the note: ")

        note = model.Note(user[0], title, description)
        store = note.store()

        if store[0] >= 1:
            print(f"Perfect you have saved the note {note.title}")
        else:
            print(f"sorry, the note has not been saved {user[1]}")
