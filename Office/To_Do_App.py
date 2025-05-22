'''
Q20) To-Do App with File Persistence 
Add, remove, mark tasks complete, and save/load from a file. 
'''

file_path = r'Output Files\tasks.csv'
def load_tasks():
    tasks = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            task_data = line.strip().split(',')
            if len(task_data) == 2:
                tasks.append({'task': task_data[0], 'complete': task_data[1] == 'True'})
    return tasks

def save_tasks(tasks):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['complete']}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for index, task in enumerate(tasks, start=1):
        status = 'Done' if task['complete'] else 'Not Done'
        print(f"{index}. {task['task']} - {status}")

def add_task(tasks):
    user_input = input('Enter your task: ').strip()
    if user_input:
        tasks.append({'task': user_input, 'complete': False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    show_tasks(tasks)
    task_number = int(input('Enter the task number to remove: ')) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['task']}")
    else:
        print("Invalid task number.")

def complete_task(tasks):
    show_tasks(tasks)
    task_number = int(input('Enter the task number to mark as complete: ')) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['complete'] = True
        save_tasks(tasks)
        print(f"Marked as complete: {tasks[task_number]['task']}")
    else:
        print("Invalid task number.")

def run_app():
    tasks = load_tasks()
    while True:
        print("\nTo-Do App Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

run_app()
