import os
import sys
import json
import traceback

STORAGE_FILE = "todo/storage.json"

def load_todo():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_todo(todo):
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

def add(todo):
    try:
        todos = load_todo()
        todos.append({"task": todo, "done": False})
        save_todo(todos)
        print("[+] todo를 추가했습니다")
    except Exception as e:
        print("[!] 오류발생", e)
        traceback.print_exc()    

def delete(todo_number:int, all:bool=False):
    todos = load_todo()
    if all:
        try:
            todos.clear()
            save_todo(todos)
            print("[-] 모든 todo를 삭제하였습니다")
        except Exception as e:
            print("[!] 오류발생", e)
    else:
        try:
            todos.pop(todo_number - 1)
            save_todo(todos)
            print("[-] todo를 삭제하였습니다")
        except Exception as e:
            print("[!] 오류발생", e)

def done(todo_number):
    try:
        todos = load_todo()
        todos[todo_number - 1]["done"] = True
        save_todo(todos)
        print("[+] 상태를 변경하였습니다")
    except Exception as e:
        print("[!] 오류발생", e)

def exit():
    sys.exit()