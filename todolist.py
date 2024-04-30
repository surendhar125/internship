# Function to display the to-do list
def display_list(todo_list):
    if todo_list:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"'{task}' added to your to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"'{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index.")

# Main function
def main():
    todo_list = []

    while True:
        print("\nTo-Do List Management")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            display_list(todo_list)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
