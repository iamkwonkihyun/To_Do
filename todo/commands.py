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
    print("Hi! Nice to meet you!")


def help():
    print("""hi      | 인사를 합니다
ls      | todo 리스트를 보여줍니다
add     | todo를 추가합니다
del     | todo를 삭제합니다
del -a  | 모든 todo를 삭제합니다
del -d  | 완료한 todo만 삭제합니다
done    | 할 일의 상태를 완료로 변경합니다
exit    | 프로그램을 종료합니다""")


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


def delete(todo_num:int, all:bool=False, done:bool=False):
    todos = load_todo()
    if all:
        try:
            todos.clear()
            save_todo(todos)
            print("[-] 모든 todo를 삭제하였습니다")
        except Exception as e:
            error_func(e)
    elif done:
        try:
            print(len(todos))
            todos = [todo for todo in todos if not todo["done"]]
            save_todo(todos)
            print("[-] 완료된 todo를 삭제하였습니다")
        except Exception as e:
            error_func(e)
    else:
        try:
            todos.pop(todo_num - 1)
            save_todo(todos)
            print("[-] todo를 삭제하였습니다")
        except Exception as e:
            error_func(e)


def done(todo_num:int):
    try:
        todos = load_todo()
        if todos[todo_num - 1]["done"]:
            todos[todo_num - 1]["done"] = False
        else:
            todos[todo_num - 1]["done"] = True
        save_todo(todos)
        print("[+] 상태를 변경하였습니다")
    except Exception as e:
        error_func(e)


def exit():
    sys.exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')