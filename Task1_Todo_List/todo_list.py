# Todo List Application

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def main():

    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
            

        elif choice == "2":
            if not tasks:
                print("No tasks available. Please add a task first.")
            else:
                show_tasks(tasks)
            

        elif choice == "3":
            if not tasks:
                 print("No tasks available to delete.")
            else:
                show_tasks(tasks)
                try:
                    num = int(input("\nEnter task number to delete: "))
                    if 0 < num <= len(tasks):
                        tasks.pop(num-1)
                        save_tasks(tasks)
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number")
                except ValueError:
                        print("Please enter a valid number")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()