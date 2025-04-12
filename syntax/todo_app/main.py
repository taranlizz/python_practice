import api


def main():
    task_list = [
        {
            "id": "1",
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "due_date": "2025-04-06 18:00",
            "priority": "HIGH",
            "creation_date": "2025-04-05 10:30",
        },
        {
            "id": "2",
            "title": "Workout",
            "description": "30-minute run and strength training",
            "due_date": "2025-04-06 07:00",
            "priority": "MEDIUM",
            "creation_date": "2025-04-05 10:45",
        },
        {
            "id": "3",
            "title": "Study Python",
            "description": "Review functions and practice exercises",
            "due_date": "2025-04-07 14:00",
            "priority": "HIGH",
            "creation_date": "2025-04-05 11:00",
        },
    ]
    is_running = True

    while is_running == True:
        print(f"\n-----TO-DO LIST-----\n")
        print("1. Show the list")
        print("2. Create a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Sort tasks by: due_date, creation_date, priority")
        print("6. Exit the program\n")

        option = input("Choose an option (1-6): ")

        match option:
            case "1":
                api.show(task_list)
            case "2":
                api.create(task_list)
            case "3":
                api.update(task_list)
            case "4":
                api.delete(task_list)
            case "5":
                api.sort(task_list)
            case "6":
                print("Exiting the program...")
                is_running = False
            case _:
                print("Invalid option type.\n")


if __name__ == "__main__":
    main()
