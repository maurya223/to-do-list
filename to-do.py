tasks = []

# Show menu
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Task add karne ke liye
def add_task():
    task = input("Enter the task: ")  # 🛠️ Input lena print nahi
    tasks.append(task)
    print("✅ Task added successfully!")

# Task delete karne ke liye
def remove_task():
    if not tasks:
        print("❌ No tasks to delete.")
        return

    view_tasks()  # pehle tasks dikhana
    try:
        tasknum = int(input("Which task number you completed? "))
        if 1 <= tasknum <= len(tasks):
            removed = tasks.pop(tasknum - 1)
            print(f"🎉 Congratulations! You completed: '{removed}'")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# View tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Main loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Goodbye! Happy Productivity!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
