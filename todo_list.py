# todo_list.py

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted successfully!")
        except IndexError:
            print("Invalid task number.")

    def mark_completed(self, task_number):
        try:
            self.tasks[task_number - 1].completed = True
            print(f"Task {task_number} marked as completed!")
        except IndexError:
            print("Invalid task number.")

    def view_all_tasks(self):
        print("\nAll Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.title} ({status})")

    def view_completed_tasks(self):
        print("\nCompleted Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            if task.completed:
                print(f"{i}. {task.title}")

    def view_pending_tasks(self):
        print("\nPending Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            if not task.completed:
                print(f"{i}. {task.title}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List App")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View All Tasks")
        print("5. View Completed Tasks")
        print("6. View Pending Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == "2":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            todo_list.view_all_tasks()
        elif choice == "5":
            todo_list.view_completed_tasks()
        elif choice == "6":
            todo_list.view_pending_tasks()
        elif choice == "7":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()