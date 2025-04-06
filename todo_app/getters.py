from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import datetime

PRIORITY_VALUES = ("LOW", "MEDIUM", "HIGH")
DATE_FORMAT = "YYYY-MM-DD-HH-MM"
AVAILABLE_TASK_FIELDS = ("title", "description", "priority", "due_date")
SORT_CRITERIA = ("due_date", "creation_date", "priority")


def get_task_by_id(task_list):
    if len(task_list) == 0:
        print("There are no items in list.")
        return None

    while True:
        task_id = prompt("Enter the id of a task to update: ")
        for task in task_list:
            if task["id"] == task_id:
                return task
        print(f"{task_id} is invalid id.")


def get_fields_list():
    while True:
        print(f"Available fields: {", ".join(AVAILABLE_TASK_FIELDS).strip()}.")

        fields_completer = WordCompleter(
            ["title", "description", "priority", "due_date"]
        )

        fields = prompt(
            "Enter the names of the fields to update (separated by commas): ",
            completer=fields_completer,
        ).lower()

        fields_list = [field.strip() for field in fields.split(",")]
        valid = True

        for field in fields_list:
            if field not in AVAILABLE_TASK_FIELDS:
                print(f"{field} is invalid field name.")
                valid = False

        if valid:
            return fields_list


def get_title(default=""):
    title = prompt("Enter a title: ", default=default)
    return title.capitalize().strip()


def get_description(default=""):
    description = prompt("Enter a description: ", default=default)
    return description.capitalize().strip()


def get_due_date(default=""):
    while True:
        try:
            raw_date = prompt(
                f"Enter the deadline date ({DATE_FORMAT}): ", default=default
            ).strip()

            date_parts = raw_date.split("-")
            if len(date_parts) != 5:
                raise ValueError(f"You must enter exactly 5 values ({DATE_FORMAT})")

            date_parts = [int(date_part) for date_part in date_parts]
            date = datetime.datetime(*date_parts)

            if date < datetime.datetime.now():
                raise ValueError("You cannot select a past date.")

            return date

        except ValueError as e:
            print(
                f"Invalid date format. Please enter a date as {DATE_FORMAT}. Error: {e}"
            )


def get_priority(default=""):
    priority_completer = WordCompleter(PRIORITY_VALUES)
    while True:
        priority = (
            prompt(
                "Select the priority level (LOW | MEDIUM | HIGH): ",
                completer=priority_completer,
                default=default,
            )
            .upper()
            .strip()
        )

        if priority not in PRIORITY_VALUES:
            print("Invalid priority value. Select the valid priority level.")
        else:
            return priority


def get_creation_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_sort_criteria():
    criteria_completer = WordCompleter(SORT_CRITERIA)
    while True:
        criteria = prompt(
            "Select the criteria (due_date, creation_date, priority): ",
            completer=criteria_completer,
        ).lower()

        if criteria not in SORT_CRITERIA:
            print("Invalid sort criteria value. Select the valid criteria.")
        else:
            return criteria
