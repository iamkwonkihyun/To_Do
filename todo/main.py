from todo.commands import greeting, ls, add, delete, exit, help, done, clear

commands = {
    "hi": greeting, 
    "ls": ls,
    "add": add,
    "del": delete,
    "exit": exit,
    "help": help,
    "done": done,
    "clear": clear,
}

def main():
    while True:
        user_input = input("todo$ ").strip()
        if user_input.startswith("add "):
            add(user_input[4:])
        elif user_input.startswith("del "):
            if user_input[4:] == "-a":
                delete(todo_number=0, all=True, done=False)
            elif user_input[4:] == "-d":
                delete(todo_number=0, all=False, done=True)
            else:
                delete(todo_number=int(user_input[4:]))
        elif user_input.startswith("done "):
            done(int(user_input[4:]))
        elif user_input in commands:
            commands[user_input]()
        else:
            print("[!] 명령어를 찾을 수 없습니다.")