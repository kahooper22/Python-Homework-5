'''
Developer: Kathryn Hooper
Date: 11 Mar 2019
This program opens a To Do list created by the user.
The program can then display, add to, or delete items
from the list. The updated list is then saved to the
file 'ToDo.txt'.
'''

#Open the To Do list created by the user
with open(r"C:\Users\Kathryn\PycharmProjects\hw5\Todo.txt") as chores:
        tasks = (chores.readlines())

#define the dictionary that will hold tasks and their priority
task_dict = {}

#read the file and add tasks and priorities to the dictionary as key, value pairs
for item in tasks:
    (key, value) = item.split(", ")
    task_dict[str(key)] = value

#begins the loop that asks the user to select an option from the menu
user_choice = 0

while user_choice != "5":
    print("Options Menu:", "\n", "1. Show current To Do List", "\n", "2. Add a new item to list", "\n", "3. Remove a completed item from list", "\n", "4. Save data to file", "\n", "5. Exit Program")

    user_choice = input("Please make a selection from the Options Menu: ")


#if user choice is one, print out the current tasks in the To Do list text file
    if user_choice == "1":
            for key, value in task_dict.items():
                    print(key + ", " + value)

#if user choice is two, add a new key, value pair to the dictionary of items
    if user_choice == "2":
            new_key = input("Please enter a new task: ")
            task_dict[new_key] = input("Please enter the priority of this task: ") + "\n"

# if the user choice is 3, prompt for an item to delete and delete if present
    if user_choice == "3":
            remove_item = input("What item would you like to remove? ")
            if remove_item in task_dict:
                del task_dict[remove_item]
                print("Item removed from To Do list.")
            else:
                print("Item not found.")
#if the user choice is 4, save current list of tasks to the ToDo text file
    if user_choice == "4":
            with open(r"C:\Users\Kathryn\PycharmProjects\hw5\Todo.txt", "w") as f:
                    for key, value in task_dict.items():
                            f.write(key + ", " + value)

            print("Thank you, data have been saved to file.")


