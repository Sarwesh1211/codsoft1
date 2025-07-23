import json
import os

# File to store tasks
TODO_FILE = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found.")
        return
    print("\n📋 Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔️ Done" if task["done"] else "❌ Not Done"
        print(f"{idx}. {task['title']} - {status}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("🟢 Task added successfully.")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks(tasks)
            print("🗑️ Task deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
