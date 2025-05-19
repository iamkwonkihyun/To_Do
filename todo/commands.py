todo_list = []

def ls():
    if not todo_list:
        print("없습니다")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add(todo):
    todo_list.append(todo)
    print("todo를 추가했습니다")

def delete(todo:int):
    try: 
        todo_list.pop(todo - 1)
        print("todo를 삭제하였습니다")
    except IndexError:
        print("다시 입력해 주세요")