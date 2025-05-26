LOW = "1"
MEDIUM = "2"
HIGH = "3"

NEW = "1"
IN_PROGRESS = "2"
DONE = "3"

STATUS = {
    NEW: "new",
    IN_PROGRESS: "in progress",
    DONE: "done"
}

PRIORITY = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}

HR = "--------------------------------------------------------------------"

tasks = {}

def load_tasks() -> None:
    global tasks
    tasks = {}
    with open("tasks.txt", "r") as file:
        for line in file:
            updated_tasks = line.split(" | ")
            task_id = updated_tasks[0]
            tasks[task_id] = {
                "ID": task_id,
                "Title": updated_tasks[1],
                "Description": updated_tasks[2],
                "Priority": updated_tasks[3],
                "Status": updated_tasks[4]
            }


def check_priority() -> str:
    priority = ""
    while priority.lower() not in PRIORITY.values():
        priority = (input("Priority (high | medium | low): "))
    return priority

def check_status() -> str:
    status = ""
    while status.lower() not in STATUS.values():
        status = (input("Status (new | in progress | done): "))
    return status

def priority_sort() -> None:
    priority = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    task_list = []

    with open("tasks.txt", "r") as file:
        for line in file:
            task_sections = line.strip().split(" | ")
            task = {
                "ID": task_sections[0],
                "Title": task_sections[1],
                "Description": task_sections[2],
                "Priority": task_sections[3].lower(),
                "Status": task_sections[4]
            }
            task_list.append(task)
    sorted_tasks = sorted(task_list, key=lambda task: priority.get(task["Priority"]))

    for task in sorted_tasks:
        print(f"{task.get('ID')} | {task.get('Title')} | {task.get('Description')} | {task.get('Priority')} | {task.get('Status')}\n")

def status_sort() -> None:
    status = {
        "new": 1,
        "in progress": 2,
        "done": 3
    }

    task_list = []

    with open("tasks.txt", "r") as file:
        for line in file:
            task_sections = line.strip().split(" | ")
            task = {
                "ID": task_sections[0],
                "Title": task_sections[1],
                "Description": task_sections[2],
                "Priority": task_sections[3],
                "Status": task_sections[4].lower()
            }
            task_list.append(task)
    sorted_tasks = sorted(task_list, key=lambda task: status.get(task["Status"]))

    for task in sorted_tasks:
        print(f"{task.get('ID')} | {task.get('Title')} | {task.get('Description')} | {task.get('Priority')} | {task.get('Status')}\n")


def add_task(task: dict) -> None:
    file = open("tasks.txt", "a")
    file.write(f"{task.get('ID')} | {task.get('Title')} | {task.get('Description')} | {task.get('Priority')} | {task.get('Status')}\n")
    file.close()

def create_task() -> None:
    task_id = int(max(tasks.keys(), default=0)) + 1
    task_title = input("Title: ")
    task_description = input("Description: ")
    task_priority = check_priority()
    task_status = check_status()
    
    tasks[task_id] = {
        "ID": task_id,
        "Title": task_title,
        "Description": task_description,
        "Priority": task_priority,
        "Status": task_status
    }
    add_task(tasks[task_id])

def name_search() -> None:
    key_word = input("Введите ключевое слово: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    updated_list = [task for task in task_list if key_word.lower() in task[1].lower() or key_word.lower() in task[2].lower()]
    if len(updated_list) == 0:
        print("Нет совпадений")
        return
    for task in updated_list:
        print(" | ".join(task) + "\n")

    
def print_tasks():
    file = open("tasks.txt", "r")
    while True:    
        choise = input("1 - Отобразить задачи в изначальном виде\n2 - Отсортировать по статусу\n3 - Отсортировать по приоритету\n4 - Осуществить поиск по названию или описанию\n0 - Вернуться назад\n")
        match choise:
            case "1":
                for line in file:
                    print(line)
            case "2":
                status_sort()
            case "3":
                priority_sort()
            case "4":
                name_search()
            case "0":
                break
    file.close()

def update_title() -> None:
    id = input("Enter task ID: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    new_title = input("Enter new title: ")

    for task in task_list:
        if task[0] == id:
            task[1] = new_title

    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(" | ".join(task))

    global tasks
    tasks = {int(task[0]): {
        "ID": int(task[0]),
        "Title": task[1],
        "Description": task[2],
        "Priority": task[3],
        "Status": task[4]
    } for task in task_list}

def update_desc() -> None:
    id = input("Enter task ID: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    new_desc = input("Enter new title: ")

    for task in task_list:
        if task[0] == id:
            task[2] = new_desc

    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(" | ".join(task))

    global tasks
    tasks = {int(task[0]): {
        "ID": int(task[0]),
        "Title": task[1],
        "Description": task[2],
        "Priority": task[3],
        "Status": task[4]
    } for task in task_list}

def update_status() -> None:
    id = input("Enter task ID: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    new_status = check_status()

    for task in task_list:
        if task[0] == id:
            task[4] = f"{new_status}\n"

    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(" | ".join(task))

    global tasks
    tasks = {int(task[0]): {
        "ID": int(task[0]),
        "Title": task[1],
        "Description": task[2],
        "Priority": task[3],
        "Status": task[4]
    } for task in task_list}

def update_priority() -> None:
    id = input("Enter task ID: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    new_priority = check_priority()

    for task in task_list:
        if task[0] == id:
            task[3] = new_priority

    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(" | ".join(task))

    global tasks
    tasks = {int(task[0]): {
        "ID": int(task[0]),
        "Title": task[1],
        "Description": task[2],
        "Priority": task[3],
        "Status": task[4]
    } for task in task_list}

def update_task():
    while True:
        choise = input("1 - название\n2 - описание\n3 - приоритет\n4 - статус\n0 - Вернуться назад\n")
        match choise:
            case "1":
                update_title()
            case "2":
                update_desc()
            case "3":
                update_priority()
            case "4":
                update_status()
            case "0":
                break

def del_task() -> None:
    id = input("Enter task ID: ")
    task_list = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_list.append(line.split(" | "))
    
    updated_list = [task for task in task_list if task[0] != id]

    if len(updated_list) == len(task_list):
        print("ID not found")
        return 

    with open("tasks.txt", "w") as file:
        for task in updated_list:
            file.write(" | ".join(task))

    global tasks
    tasks = {task[0]: {
        "ID": task[0],
        "Title": task[1],
        "Description": task[2],
        "Priority": task[3],
        "Status": task[4]
    } for task in updated_list}

def main():
    load_tasks()
    while True:
        choise = input("1 - Создать новую задачу\n2 - Просмотреть задач\n3 - Обновить задачу\n4 - Удалить задачу\n0 - Выйти из программы\n")
        match choise:
            case "1":
                create_task()
            case "2":
                print_tasks()
            case "3":
                update_task()
            case "4":
                del_task()
            case "0":
                break

if __name__ == "__main__":
    main()
