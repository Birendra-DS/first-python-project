# welcome message
print('Welcome to task tracker!')
# Ask user how many tasks they planned for today
count_task = int(input('Please Enter how many task you planned for today:'))

# create and empty list to store the tasks
tasks = []
# use a loop to take the input of each task from the user and append this to tasks list
for i in range(count_task):
    task = input("Enter your task name:")
    tasks.append(task)
print('Here are you planned task list:',tasks)  # it prints all task at once 

# create another list to store the completed tasks
completed_tasks = []

# ask the user which task are completed and then append the completed task to new list 
for task in tasks: 
    finished_tasks = input(f"Did you complete {task}: (yes/no):") # also try to write my own version
    #finished_tasks = input('Did you complete',task, ':yes/No:') # it gives error because input only take atmost 1 argumant here we give it 3

    if (finished_tasks.lower() == "yes"):
        completed_tasks.append(task)
    
        
#Finally, print all completed task
print("\nhere are completed task:") # \n is like a line-break.It makes the output clearer and more readable.
for task in completed_tasks:
    print("->" + task)

n = input('Enter your name:')
d = input('Enter your future goal:')
min_task = int(input('How many tasks should you complete today to be proud:'))
if (len(completed_tasks) < min_task):    
    print('come on',n,'otherwise your',d,'dream will misssed')
else: 
    print('🎉🎉🎉 well done, keep it up and stay focused. You are one step closer to your dream',d,)



