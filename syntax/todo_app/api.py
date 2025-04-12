import uuid
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import datetime
import getters


def show(task_list):
    print("\n TO-DO LIST \n")
    task_ls_length = len(task_list)

    if task_ls_length == 0:
        print("\nThere are no tasks in your list!\n")
        return

    print()

    for i in range(task_ls_length):
        print(f"{i+1}.", end=" ")
        for key, value in task_list[i].items():
            print(f"\t{key.title()}: {value}")
        print()


def create(task_list):
    task = {}

    task["id"] = str(uuid.uuid4())[:10]
    task["title"] = getters.get_title()
    task["description"] = getters.get_description()
    task["priority"] = getters.get_priority()
    task["due_date"] = getters.get_due_date()
    task["creation_date"] = getters.get_creation_date()

    task_list[0] = task
    print("\nSuccess! The task was added to your list.\n")

    return task_list[0]


def update(task_list):
    task = getters.get_task_by_id(task_list)

    if task is None:
        return

    fields_to_update_list = getters.get_fields_list()

    get_functions = {
        "title": getters.get_title,
        "description": getters.get_description,
        "priority": getters.get_priority,
        "due_date": getters.get_due_date,
    }

    for field in fields_to_update_list:
        task[field] = get_functions[field](task[field])

    task["update_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nSuccess! The task has been updated.\n")
    for key, value in task.items():
        print(f"{key}: {value}")


def delete(task_list):
    task_to_delete = getters.get_task_by_id(task_list)

    if task_to_delete is None:
        return

    task_list.remove(task_to_delete)
    print("\nSuccess! Task was deleted.\n")
    return task_to_delete


def sort(task_list):
    criteria = getters.get_sort_criteria()
    priority = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
    match criteria:
        case "due_date" | "creation_date":
            task_list.sort(key=lambda task: task[criteria])
        case "priority":
            task_list.sort(key=lambda task: priority[task[criteria]], reverse=True)
    print("\nSuccess! The list was sorted by the selected criteria.\n")
