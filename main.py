import task 
import tasklist
import check_input

def main_menu():
    print(f'-Tasklist-\n'
            'Tasks to complete: {}\n' 
            '1. Display current task\n'
            '2. Display all tasks\n'
            '3. Mark current task complete\n'
            '4. Add new task\n'
            '5. Search by date\n'
            '6. Save and quit\n')
    

def get_date():
    print('Enter due date:')
    month = check_input.get_int_range('Enter month: ', 1, 12)
    day = check_input.get_int_range('Enter day: ', 1, 31)
    year = check_input.get_int_range('Enter year: ', 2000, 2100)
    return f'{month:01d}/{day:01d}/{year}'

def get_time():
    print('Enter time:')
    hour = check_input.get_int_range('Enter hour: ', 0, 23)
    minute = check_input.get_int_range('Enter day: ', 0, 59)
    return f'{hour:01d}:{minute:01d}'

def main():
    tasks = tasklist.Tasklist()
    main_menu()

    
        
main() 


    


