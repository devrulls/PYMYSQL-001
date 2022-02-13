from user import actions
print("""
Actions available
    - register
    - login
""")
toDo = actions.Actions()

action = input("what you want to do? ")
if action == 'register':
    toDo.register()
elif action == 'login':
    toDo.loginUser()
