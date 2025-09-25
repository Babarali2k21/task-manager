from .storage import load_tasks, save_tasks


def add_task(title, description="", priority="Medium", due_date=None):
    tasks = load_tasks()
    new_id = 1 if not tasks else max(t["id"] for t in tasks) + 1

    task = {
        "id": new_id,
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks(show_completed=None):
    tasks = load_tasks()
    if show_completed is None:
        return tasks
    return [t for t in tasks if t["completed"] == show_completed]


def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_tasks(tasks)
            return t
    return None


def delete_task(task_id):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            return removed
    return None
