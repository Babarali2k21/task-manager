from src.manager.task import add_task, list_tasks, complete_task, delete_task

def main():
    print("Task Manager CLI")
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose (1/2/3/4/5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            priority = input("Enter priority (Low/Medium/High): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = add_task(title, description, priority, due_date)
            print(f"Added: {task}")

        elif choice == "2":
            tasks = list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nTasks:")
                for t in tasks:
                    status = "Completed" if t["completed"] else "<Not Completed"
                    print(f"ID {t['id']}: {t['title']} [{status}] - {t['priority']} (Due: {t['due_date']})")

        elif choice == "3":
            task_id = int(input("Enter task ID to mark completed: "))
            updated = complete_task(task_id)
            if updated:
                print(f"Marked as completed: {updated['title']}")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            removed = delete_task(task_id)
            if removed:
                print(f"Deleted: {removed['title']}")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
