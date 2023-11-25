import os

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print(f"Added task: '{new_task}'")
        self.save_tasks()

    def delete_task(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task number.")
        else:
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Deleted task: '{deleted_task}'")
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def load_tasks(self):
        tasks = []
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
        return tasks

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("="*30)
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")
        print("="*30)

        choice = input("Enter option number: ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            new_task = input("Enter new task: ")
            todo_list.add_task(new_task)
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
