# ==========================================
# TASK MANAGEMENT SYSTEM
# STACK + QUEUE IMPLEMENTATION
# ==========================================

# Queue for task scheduling (FIFO)
task_queue = []

# Stack for undo operations (LIFO)
undo_stack = []


# ==========================================
# ADD TASK
# ==========================================

def add_task(task):
    task_queue.append(task)
    print("Task added:", task)


# ==========================================
# PROCESS TASK
# ==========================================

def process_task():
    if len(task_queue) > 0:
        task = task_queue.pop(0)
        undo_stack.append(task)
        print("Processed task:", task)
    else:
        print("No tasks to process")


# ==========================================
# UNDO TASK
# ==========================================

def undo_task():
    if len(undo_stack) > 0:
        task = undo_stack.pop()
        print("Undo last processed task:", task)
    else:
        print("Nothing to undo")


# ==========================================
# SHOW TASKS
# ==========================================

def show_tasks():
    print("\nPending Tasks (Queue):", task_queue)
    print("Undo Stack:", undo_stack)


# ==========================================
# MENU DRIVEN PROGRAM
# ==========================================

while True:

    print("\n====== TASK MANAGER ======")
    print("1. Add Task")
    print("2. Process Task")
    print("3. Undo Task")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        process_task()

    elif choice == "3":
        undo_task()

    elif choice == "4":
        show_tasks()

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")