print("""
Actions available
    - register
    - login
""")

action = input("what you want to do? ")

if action == 'register':
    print("\nGreat, we will proceed to register you in our system.")
    name = input("What is your name: ");
    last_name = input("What is your Last name: ");
    email = input("What is your email: ");
    password = input("Enter your password: ");

elif action =='login':
    print("\nCool, please login")
    email = input("What is your email: ");
    password = input("Enter your password: ");