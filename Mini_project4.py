


    




# Initialize task list globally
task = []

print("---WELCOME TO THE TASK MANAGEMENT APP----")

# Getting the number of tasks
total_tasks = int(input("Enter how many tasks you want to do today = "))
for i in range(1, total_tasks + 1):      
    task_name = input(f"Enter task {i}: ")
    task.append(task_name)


print(f"Today's tasks are: {task}")  

# Task management operations
while True:
    operation = int(input("Enter 1- Add\n2- Update\n3- Delete\n4- View\n5- Exit/Stop\n"))
    
    if operation == 1:
        add = input("Enter the task you want to add = ")
        task.append(add)
        print(f"Task '{add}' successfully added...")
    
    elif operation == 2:
        updated_val = input("Enter the task name you want to update = ")
        if updated_val in task:
            up = input("Enter the new task = ")
            ind = task.index(updated_val)  # For getting index number 
            task[ind] = up
            print(f"Task '{updated_val}' updated to '{up}'")
        else:
            print(f"Task '{updated_val}' not found.")
    
    elif operation == 3:
        del_val = input("Which task do you want to delete: ")
        if del_val in task:
            ind = task.index(del_val)  # For getting index number
            del task[ind]
            print(f"Task '{del_val}' has been deleted.")
        else:
            print(f"Task '{del_val}' not found.")
    
    elif operation == 4:
        print(f"Total tasks: {task}")
    
    elif operation == 5:
        print("Closing program...")
        break
    
    else:
        print("Invalid input.")
