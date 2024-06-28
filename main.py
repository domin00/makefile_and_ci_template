import sys


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Added task: "{task}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Deleted task: "{removed_task}"')
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()

    while True:
        command = input("Enter a command (add/view/delete/exit): ").strip().lower()

        if command == "add":
            task = input("Enter a task: ").strip()
            todo_list.add_task(task)
        elif command == "view":
            todo_list.view_tasks()
        elif command == "delete":
            try:
                task_number = int(input("Enter the task number to delete: ").strip())
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "exit":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Unknown command. Please use add/view/delete/exit.")


if __name__ == "__main__":
    main()
