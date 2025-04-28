import task 
import check_input

def main_menu():
    print(f'-Tasklist- '
            'Tasks to complete: {}' 
            '1. Display current task'
            '2. Display all tasks'
            '3. Mark current task complete'
            '4. Add new task'
            '5. Search by date'
            '6. Save and quit')

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
    with open('tasklist-1.txt', 'rw') as f:
        list = f.readlines()
        


    


