from todo.commands import ls, add, delete    
commands = {
    "ls": ls,
    "add": add,
    "del": delete,
}

def main():
    while True:
        user_input = input(">>> ").strip()
        if user_input.startswith("add "):
            add(user_input[4:])
        elif user_input.startswith("del "):
            delete(int(user_input[4:]))
        elif user_input in commands:
            commands[user_input]()
        else:
            print("명령어를 찾을 수 없습니다.")