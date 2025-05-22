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
        user_input = input("todo$ ")
        cmd, _, value = user_input.partition(" ")
        if cmd == "add":
            add(value)
        elif cmd == "del":
            if value == "-a":
                delete(todo="0", all=True, done=False)
            elif value == "-d":
                delete(todo="0", all=False, done=True)
            else:
                delete(todo=value)
        elif cmd == "done":
            done(value)
        elif user_input in commands:
            commands[user_input]()
        else:
            print("[!] 명령어를 찾을 수 없습니다.")