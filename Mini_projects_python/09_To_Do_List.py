tasks = []

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print("Task added successfully!")
    

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour TO-Do List: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task {removed} deleted successfully!")
                
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
while True:
    print("\n--- TO_Do LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye! Have a productive day!😊")
        break  
    else:
        print("Invalid choice. Please try again.")      
        