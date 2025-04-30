import task 
import tasklist
import check_input

def main_menu(num_tasks):
    """
    Displays the main menu and returns the user's choice."""
    print(f'-Tasklist-\n'
            f'Tasks to complete: {num_tasks} \n' 
            '1. Display current task\n'
            '2. Display all tasks\n'
            '3. Mark current task complete\n'
            '4. Add new task\n'
            '5. Search by date\n'
            '6. Save and quit\n')
    choice = check_input.get_int_range('Enter choice: ', 1, 6)
    return choice
    

def get_date():
    """
    Prompts the user for a date and returns it in the format MM/DD/YYYY.
    """
    print('Enter due date:')
    month = check_input.get_int_range('Enter month: ', 1, 12)
    day = check_input.get_int_range('Enter day: ', 1, 31)
    year = check_input.get_int_range('Enter year: ', 2000, 2100)
    return f'{month:01d}/{day:01d}/{year}'

def get_time():
    """
    Prompts the user for a time and returns it in the format HH:MM.
    """
    print('Enter time:')
    hour = check_input.get_int_range('Enter hour: ', 0, 23)
    minute = check_input.get_int_range('Enter minute: ', 0, 59)
    return f'{hour:01d}:{minute:01d}'

def main():
    """
    Main function to run the task list program."""

    # Initialize the task list
    tasks = tasklist.Tasklist()
    choice = 0 
    while choice != 6: 
        choice = main_menu(len(tasks))

        
        if choice == 1: 
            # Display the current task
            print(f'{tasks.get_current_task()}\n')
        elif choice == 2:
            # Display all tasks
            count = 1 
            for task in tasks: 
                print(f"{count}. {task}")
                count+=1
            print()
        elif choice == 3: 
            # Mark the current task as complete
            # And display the new current task
            print(f'Marking current task as complete: {tasks.get_current_task()}') 
            tasks.mark_complete()
            print(f'New current task is: {tasks.get_current_task()}\n')

        elif choice == 4: 
            # Add a new task
            desc = input('Enter a task: ') 
            date = get_date()
            time = get_time() 
            tasks.add_task(desc, date, time)
            print() 
        
        elif choice == 5:
            # Search for tasks by date
            # Display all tasks due on that date  
            date = get_date()
            print(f'Tasks due on {date}:')
            count = 1 
            for task in tasks: 
                task_month, task_day, task_year = map(int, task._date.strip().split('/'))
                search_month, search_day, search_year = map(int, date.strip().split('/'))
    
                if (task_month == search_month and 
                    task_day == search_day and 
                    task_year == search_year): 
                    print(f"{count}. {task}")
                    count+=1
            print()
        
main() 


    


