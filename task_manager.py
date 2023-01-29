# Note use the following username and password to access the admin rights 
# username: admin
# password: password
#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    '''This function allows a new user and password to be added to the user.txt file'''
    
    while True:
        # - Request input of a new username
        new_username = input("New Username: ")
        # - Check whether user name already in use 
        if new_username in username_password:
            # if name already in use, loops back to ask for new_username again until different
            print("That user name is already in use.")
        
        else:
            # - Request input of a new password
            new_password = input("New Password: ")

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password
                # update the user.txt file for the new user and password
                with open("./T21/DS T21 updated task files/user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
                break
            # - Otherwise you present a relevant message.
            else:
                print("Passwords do no match")
                break
    

def add_task(task_list):
    '''This function allows a user to add a new task to task.txt file'''
    # - Prompt a user for the following: 
    #     - A username of the person whom the task is assigned to,
    #     - A title of a task,
    #     - A description of the task and 
    #     - the due date of the task.
    while True:
        task_username = input("Name of person assigned to task: ")
    
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        else:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


    # - Then get the current date.
    curr_date = date.today()
    # - Add the data to the file task.txt and
     # - You must remember to include the 'No' to indicate if the task is complete.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
        }
    #update tasks.txt by iterating through task_list and adding each task as a list (str_attrs)
    #to the overall list task_list_to_write
    task_list.append(new_task)
    with open("./T21/DS T21 updated task files/tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
                ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    #This function allows the program to read the tasks from task.txt file and
    #print to the console in the format of Output 2 presented in the task pdf (i.e. include spacing and labelling) 
    #go through each task in the task list and print out in the required format
    print("----------------------------------------")
    for t in task_list:
        disp_str = f"Task: \t\t\t {t['title']}\n"
        disp_str += f"Assigned to: \t\t {t['username']}\n"
        disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \t {t['description']}\n"
        print(disp_str)
        print("----------------------------------------")    


def view_mine():
    #In this block you will put code the that will read the task from task.txt file and
    #print to the console in the format of Output 2 presented in the task pdf (i.e. include spacing and labelling)
    #iterate through task_list and pull out only tasks assigned to curr_user
    
    print("-------------------------------------------")
    for t in task_list:
        if t['username'] == curr_user:
            disp_str =  f"Task number: \t\t {t['task number']}\n"
            disp_str += f"Task: \t\t\t {t['title']}\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            disp_str += f"Task Complete: \t\t {'Yes' if t['completed'] else 'No'}"
            print(disp_str)
            print("-------------------------------------------")  
            
     #ask the user to select either amend a task by entering the task number or return to main menu        
    task_select = int(input('''To amend a task or mark as complete please enter the task number, or -1 to return to main menu '''))
    #return to main menu
    if task_select == -1:
        print("Main menu: ")
    #pre-empting out of range requests
    elif task_select > task_number:
        print("Task number out of range")
    # for ease of use print the task out again
    #use the task number to select the title of the task and ask the user what amendment to make
    else:
        print("-----------------------------------------------")
        print(f"\
Task number:      {task_select}\n\
Task:             {task_list[(task_select - 1)]['title']}\n\
Assigned to:      {task_list[(task_select - 1)]['username']}\n\
Date assigned:    {task_list[(task_select - 1)]['assigned_date']}\n\
Due Date:         {task_list[(task_select - 1)]['due_date']}\n\
Task Description: {task_list[(task_select - 1)]['description']}\n\
        -----------------------------------------------   \n")

        amend = input('''Please select from the following:
        Enter 1  -  To mark the task as complete 
        Enter 2  -  To amend the username
        Enter 3  -  To amend the due date\n''')
        #check whether the task is already completed and therefore can't be altered
        if task_list[(task_select - 1)]['completed'] == True:
            print("Completed tasks cannot be edited")
        else:
            #set the task to completed
            if amend == '1':
                task_list[(task_select-1)]['completed'] = True
            #ask for the new username for teh task and update the dictrionary task_list
            elif amend == '2':
                amend_user = input("Please enter the new username for this task: ")
                task_list[(task_select - 1)]['username'] = amend_user
            #ask for the revised due date and update the dictionary task_list
            else:
                amend_date = input("Please enter a revised due date for this task: ")
                due_date_time = datetime.strptime(amend_date, DATETIME_STRING_FORMAT)
                task_list[(task_select - 1)]['due_date'] = due_date_time


def gen_reports(task_list):
    # This function creates a file task_overview.txt which returns various task list statistics as 
    # set out in T21 task pdf
    total_tasks = len(task_list)
    no_completed_tasks = 0
    no_unfinished_tasks = 0
    no_overdue_tasks = 0
    curr_date = datetime.today()
    # iterate through the task list and count the number of completed tasks, unfinished tasks and overdue tasks
    for task in task_list:
        if task['completed'] == True:
            no_completed_tasks += 1
        else: 
            no_unfinished_tasks += 1
            if task['due_date'] < curr_date:
                no_overdue_tasks += 1
    percentage_incomplete = no_unfinished_tasks/total_tasks * 100
    percentage_overdue = no_overdue_tasks/total_tasks * 100

    # open the file and write in the data in an easy to read format
    with open("./T21/DS T21 updated task files/task_overview.txt", 'w') as task_overview:
        task_overview.write(f"Task Overview: \n\n\
Number of tasks created:                {total_tasks:>25} \n\
Number of completed tasks:              {no_completed_tasks:>25} \n\
Number of incomplete tasks:             {no_unfinished_tasks:>25} \n\
Number of incomplete and overdue tasks: {no_overdue_tasks:>25} \n\
Percentage of tasks incomplete:         {percentage_incomplete:>25}% \n\
Percentage of tasks overdue:            {percentage_overdue:>25}%  ")


def display_stats(curr_user, user_data, task_list):
    # This function creates a file called user_overview.txt which contains information specific to the 
    # logged in user about the tasks assigned to them, as per the pdf instructions
    number_users = len(user_data)
    total_tasks = len(task_list)
    curr_user_tasks = 0
    curr_user_completed_tasks = 0
    curr_user_incomplete = 0
    curr_user_overdue_tasks = 0
    # iterate through the task list, picking out tasks assigned to the current user and counting up 
    # the number of complete, unfinished and overdue tasks 
    for task in task_list:
        if task['username'] == curr_user:
            curr_user_tasks += 1
            if task['completed'] == True:
                curr_user_completed_tasks += 1
            else:
                curr_user_incomplete += 1
                if task['due_date'] < datetime.today():
                    curr_user_overdue_tasks += 1
    percentage_tasks_curr_user = curr_user_tasks/total_tasks * 100
    user_percentage_completed = curr_user_completed_tasks/curr_user_tasks * 100
    user_percentage_incomplete = 100 - user_percentage_completed
    user_percentage_overdue = curr_user_overdue_tasks/curr_user_incomplete * 100

    # open the file and write in the required information in an easy to read format
    with open("./T21/DS T21 updated task files/user_overview.txt", 'w') as user_overview:
        user_overview.write(f"User Overview for {curr_user}: \n\n\
Number of tasks assigned to you:             {curr_user_tasks:>25}\n\
Percentage of all tasks assigned to you:     {percentage_tasks_curr_user:>25}%\n\
Percentage of your tasks completed:          {user_percentage_completed:>25}%\n\
Percentage of your tasks still to complete:  {user_percentage_incomplete:>25}%\n\
Percentage of your tasks which are overdue:  {user_percentage_overdue:>25}%   ")

#======Program Start=======
# Create tasks.txt if it doesn't exist
if not os.path.exists("./T21/DS T21 updated task files/tasks.txt"):
    with open("./T21/DS T21 updated task files/tasks.txt", "w") as default_file:
        pass

# open tasks.txt and create a list called task_data - each line of the file will be an item in the list
with open("./T21/DS T21 updated task files/tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# create a list called task_list and add in a dictionary for each task (line) in the main file
# this section includes adding a task number to each task and storing that with the rest of the task data in the dictionary
task_list = []
task_number = 0
for t_str in task_data:
    curr_t = {}
    task_number += 1
    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['task number'] = task_number
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
    


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# If no user.txt file, write one with a default account
if not os.path.exists("./T21/DS T21 updated task files/user.txt"):
    with open("./T21/DS T21 updated task files/user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("./T21/DS T21 updated task files/user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# create a while loop to enable repeated login questions until correct information is entered
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    
    # check if the username is one of the registered users
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    else:
        curr_pass = input("Password: ")
    # check the password against the password held in the dictionary for that user
    if username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#======= user menu section ======
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        # call on the reg_user function at start of program
        new_user = reg_user()
        
    elif menu == 'a':
        # a call on the add_task function to add a task to the file
        new_task = add_task(task_list)

    elif menu == 'va':
        # a call on the view_all function to view all tasks on screen
        view_all()

    elif menu == 'vm':
        #a call on the view_mine function which returns on screen the tasks assigned to the current user
        view_mine()

    elif menu == 'gr':
        # a call on the gen_reports function which creates a file task_overview.txt 
        gen_reports(task_list)

    elif menu == 'ds':
        # check whether the task_overview file has already been created and generate it if not
        if not os.path.exists("./T21/DS T21 updated task files/task_overview.txt"):
            gen_reports(task_list)
        # a call on the display_stats function which creates the user_overview.txt file
        display_stats(curr_user, user_data, task_list)
        # printing the information to the screen for the admin user only
        if curr_user == 'admin':
            print("-"*80)
            with open("./T21/DS T21 updated task files/task_overview.txt", 'r') as task_file:
                for lines in task_file:
                    print(lines)
                print("-"*80)
            with open("./T21/DS T21 updated task files/user_overview.txt", 'r') as user_file:
                for lines in user_file:
                    print(lines)
                print("-"*80)

    elif menu == 'e':
        # exit the program
        print('Goodbye!!!')
        exit()

    else:
        # to catch any incorrect choices
        print("You have made a wrong choice, please try again")