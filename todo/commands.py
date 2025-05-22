import os
import sys
import json
import traceback

STORAGE_FILE = "todo/storage.json"

def error_func(e):
    print("[!] 오류발생", e)
    traceback.print_exc()


def load_todo():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []


def save_todo(todo:list):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(todo, f, ensure_ascii=False, indent=2)


def greeting():
    print("Hi! Nice to meet you! if you need help, use the \"help\" command")


def help():
    print("""hi      | 인사를 해줍니다 ( hi )
ls      | todo 리스트를 보여줍니다 ( ls )
add     | todo를 추가합니다 ( add <todo> )
del     | todo를 삭제합니다 ( del <todo> )
del -a  | 모든 todo를 삭제합니다 ( del -a )
del -d  | 완료한 todo만 삭제합니다 ( del -d )
done    | 할 일의 상태를 완료로 변경합니다 ( done <todo> )
exit    | 프로그램을 종료합니다 ( exit )""")


def ls():
    todos = load_todo()
    if len(todos):
        print("{:<10}{:<10}{:<10}".format("number", "status", "task"))
        print("---------------------------")
        for idx, todo in enumerate(todos, start=1):
            status = "O" if todo.get("done") else "X"
            print("{:<10}{:<10}{:<10}".format(idx, status, todo.get('task')))
    else:
        print("[!] todo가 없습니다")


def add(todo:list):
    try:
        todos = load_todo()
        todos.append({"task": todo, "done": False})
        save_todo(todos)
        print("[+] todo를 추가했습니다")
    except Exception as e:
        error_func(e)   


def delete(todo:str, all:bool=False, done:bool=False):
    todos = load_todo()
    
    if todo.isdigit():
        todo = int(todo)
    
    if all:
        try:
            todos.clear()
            save_todo(todos)
            print("[-] 모든 todo를 삭제하였습니다")
        except Exception as e:
            error_func(e)
    elif done:
        try:
            todos = [todo for todo in todos if not todo["done"]]
            save_todo(todos)
            print("[-] 완료된 todo를 삭제하였습니다")
        except Exception as e:
            error_func(e)
    else:
        if isinstance(todo, int):
            try:
                todos.pop(todo - 1)
                save_todo(todos)
                print("[-] todo를 삭제하였습니다")
            except Exception as e:
                error_func(e)
        elif isinstance(todo, str):
            try:
                todos = [item for item in todos if item["task"] != todo]
                save_todo(todos)
                print("[-] todo를 삭제하였습니다")
            except Exception as e:
                error_func(e)


def done(todo:str):
    todos = load_todo()
    
    if todo.isdigit():
        todo = int(todo)

    try:
        if isinstance(todo, int) and 0 <= todo - 1 < len(todos):
            todos[todo - 1]["done"] = not todos[todo - 1]["done"]
            save_todo(todos)
            print("[+] 상태를 변경하였습니다")
        elif isinstance(todo, str):
            for item in todos:
                if item["task"] == todo:
                    item["done"] = not item["done"]
                    break
                save_todo(todos)
                print("[+] 상태를 변경하였습니다")
        else:
            print("[!] 잘못된 값입니다")
    except Exception as e:
        error_func(e)


def exit():
    sys.exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')