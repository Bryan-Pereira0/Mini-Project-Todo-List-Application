# Function to add a task.
def add_task(tasks_list):
    while True:
        task_name = input("Enter the task you want to add: ")
        if task_name:
            tasks_list.append({"title": task_name, "status": "Incomplete"})
            print(f"{task_name} has been added to your list!")
            break
        else:
            print("Please enter something.")


# Function to view tasks.
def view_task(tasks_list):   
    if len(tasks_list) == 0:
        print("The list is empty")
    else:
        if tasks_list:
            print("Your To-Do list: ")
            index = 1
            for task in tasks_list:
                print(f"{[index]}. {task["title"]} - {task["status"]}")
                index += 1
                    

# Function to mark a task as complete.
def complete_task(tasks_list):
    if tasks_list:
            print("Your To-Do list: ")
            index = 1
            for task in tasks_list:
                print(f"{[index]}. {task["title"]} - {task["status"]}")
                index += 1
    while True:
        try:
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks_list):
                tasks_list[task_number]["status"] = "Complete"
                print(f"Task '{tasks_list[task_number]['title']}' marked as complete.")
                break
            else:
                print("Invalid task number.")
                break
        except ValueError:
            print("Please enter a valid number.")
            break


# Function to delete a task.
def delete_task(tasks_list):
    if tasks_list:
                print("Your To-Do list: ")
                index = 1
                for task in tasks_list:
                    print(f"{[index]}. {task["title"]} - {task["status"]}")
                    index += 1  
    while True:        
        try:
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 < task_number < len(tasks_list):
                removed_task = tasks_list.pop(task_number)
                print(f"Task '{removed_task['title']}' deleted successfully.")
                break
            else:
                print("The list is empty.")
                break
        except ValueError:
            print("Please enter a valid number.")
            break


# Main function to run the To-Do list.
def to_do_list():
    tasks_list = []  # The main list to add and remove tasks from
    while True:
        print("Welcome to the To-Do List App!")
        print("Menu: ")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks_list)
            elif choice == 2:
                view_task(tasks_list)
            elif choice == 3:
                complete_task(tasks_list)
            elif choice == 4:
                delete_task(tasks_list)
            elif choice == 5:
                print("Thank you for using the To-Do List App. Goodbye!")
                break
            else:
                print("Please choose one of the options listed (1-5).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Run the To-Do List application.
to_do_list()