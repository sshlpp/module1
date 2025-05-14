LOW = "1"
MEDIUM = "2"
HIGH = "3"
STATUS = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}

tasks = {}

def add_task(task):
    file = open("tasks.txt", "w")
    file.write(f"{task.get('ID')} | {task.get('Title')} | {task.get('Description')} | {task.get('Priority')} | {task.get('Status')}")
    file.close()

def create_task():
    task_id = len(tasks) + 1
    task_title = input("Title:")
    task_description = input("Description:")
    task_priority = input("Priority:")
    task_status = input("Status:")
    
    tasks[task_id] = {
        "ID": task_id,
        "Title": task_title,
        "Description": task_description,
        "Priority": task_priority,
        "Status": task_status
    }
    add_task(tasks[task_id])
    

def print_tasks():
    file = open("tasks.txt", "r")
    content = file.read()
    print(f"-----------------------------\n{content}\n_____________________________\n")

# def update_task():

# def del_task():


def main():
    while True:
        choise = input("1 - Создать новую задачу\n2 - Просмотреть задач\n3 - Обновить задачу\n4 - Удалить задачу\n0 - Выйти из программы\n")
        match choise:
            case "1":
                create_task()
            case "2":
                print_tasks()
            # case "3":
            #     update_task():
            # case "4":
            #     del_task():
            case "0":
                break




#     1 - Создать новую задачу
#     2 - Просмотреть задач
#     3 - Обновить задачу
#     4 - Удалить задачу
#     0 - Выйти из программы

if __name__ == "__main__":
    main()

