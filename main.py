import task 
import tasklist
import check_input

def main_menu(num_tasks):
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
    print('Enter due date:')
    month = check_input.get_int_range('Enter month: ', 1, 12)
    day = check_input.get_int_range('Enter day: ', 1, 31)
    year = check_input.get_int_range('Enter year: ', 2000, 2100)
    return f'{month:01d}/{day:01d}/{year}'

def get_time():
    print('Enter time:')
    hour = check_input.get_int_range('Enter hour: ', 0, 23)
    minute = check_input.get_int_range('Enter minute: ', 0, 59)
    return f'{hour:01d}:{minute:01d}'

def main():
    tasks = tasklist.Tasklist()
    choice = 0 
    while choice != 6: 
        choice = main_menu(len(tasks))

        if choice == 1: 
            print(f'{tasks.get_current_task()}\n')
        elif choice == 2:
            count = 1 
            for task in tasks: 
                print(f"{count}. {task}")
                count+=1
            print()
        elif choice == 3: 
            print(f'Marking current task as complete: {tasks.get_current_task()}') 
            tasks.mark_complete()
            print(f'New current task is: {tasks.get_current_task()}\n')

        elif choice == 4: 
            desc = input('Enter a task: ') 
            date = get_date()
            time = get_time() 
            tasks.add_task(desc, date, time)
            print() 
        
    
            
        
    
        
main() 


    


