tasks = []

def showlist():
    if not tasks:
        print("Your list is empty. \nwrite something :)")
    else:
        print("Enter your list:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def add():
    a = input("Enter a task to add: ")
    tasks.append(a)
    print(f"Task '{a}' added to the list.")

def delete():
    showlist()
    if tasks:
        task_no = int(input("Enter the task number you want to remove from the list: ")) - 1
        if 0 <= task_no < len(tasks):
            print(f"Task '{tasks.pop(task_no)}' is deleted from the list.")
        else:
            print("Invalid task number.")

def update():
    task_no = int(input("Enter the task number to be updated: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no] = input("Enter the new task: ")
        print("Task updated.")
    else:
        print("Invalid task no.")

def main():
    while True:
        print("1-. Display the List")
        print("2-. To Add task")
        print("3-. TO  Delete Task")
        print("4-. To Update  Task")
        
        choice = int(input("Choose between 1-4: "))

        if choice == 1:
            showlist()
        elif choice == 2:
            add()
        elif choice == 3:
            delete()
        elif choice == 4:
            update()
        else:
            print("Invalid choice. Please select between 1-4.")

if __name__ == "__main__":
    main()