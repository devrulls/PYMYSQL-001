import user.user as model
import notes.actions


class Actions:

    def register(self):
        print("\nGreat, we will proceed to register you in our system.")
        name = input("What is your name: ")
        last_name = input("What is your Last name: ")
        email = input("What is your email: ")
        password = input("Enter your password: ")

        # creo un nuevo usuario, llamando al constructor de mi class User
        user = model.User(name, last_name, email, password);
        register = user.register();

        if register[0] >= 1:
            print(f"\nPerfect {register[1].name}!!!, you have registered with your email address {register[1].email}")
        else:
            print("\nError - you have not successfully registered")

    def loginUser(self):
        print("\nCool, please login")
        try:
            email = input("What is your email: ")
            password = input("Enter your password: ")

            user = model.User('', '', email, password)
            login = user.login()

            if email == login[3]:
                print(f"\nWelcome {login[1]} you have registered in the system on {login[5]}")
                self.other_actions(login)
            else:
                print("ERROR")
        except Exception as e:
            # print(type(e));
            # print(type(e).__name__);
            print(f"Incorrect login");

    def other_actions(self, user):
        print("""
        Actions available:
            - Create Note (create)
            - Display Notes (show)
            - Remove Notes (remove)
            - Exit (exit)
        """)
        action = input("what you want to do? ")
        toDo = notes.actions.Actions()
        if action == "create":
            toDo.create(user);
            self.other_actions(user);

        elif action == "show":
            print(f"show")
            self.other_actions(user);

        elif action == "remove":
            print(f"remove")
            self.other_actions(user);

        elif action == "exit":
            print(f"Exit");
            exit();


