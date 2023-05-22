


import json


def load_tasks():
    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file)

def add_tasks(tasks):
    title =input("Enter the Task Title: ")
    description = input("Enter the Task Discription: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully! ")

def complete_task(tasks):
    task_index = int(input("Enter the task index to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def delete_task(tasks):
    task_index = int(input("Enter the task index to delete: "))
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print("Task deleted successfully!")
        print("Deleted Task Details:")
        print(f"Title: {deleted_task['title']}")
        print(f"Description: {deleted_task['description']}")
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{index},{task['title']} - {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Deleted Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()