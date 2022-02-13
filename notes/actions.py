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

    def show(self, user):
        print(f"\nok {user[1]}!!, here are your notes..")

        note = model.Note(user[0], "", "")
        notes = note.readByUserId();

        for nota in notes:
            print(f"Title: {nota[2]} and description notes: {nota[3]} ");

    def remove(self, user):
        print(f"\nok {user[1]}!!, let's remove a note..")
        title = input("Enter the title of the note to be deleted: ")

        note = model.Note(user[0], title, "")
        remove = note.remove()

        if remove[0] >= 1:
            print(f"We have deleted the note title: {title}");
        else:
            print(f"Error - Note has not been deleted");




