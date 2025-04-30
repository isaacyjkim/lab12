class Task:

    """
    A class to represent a task with a description, date, and time.
    """
    def __init__(self, desc, date, time):
        # This method initializes the task with a description, date, and time.
        self._description = desc
        self._date = date
        self._time = time
    

    
    def __str__(self):
        # This method returns a string representation of the task.
        return (f'{self._description} - Due: {self._date} at {self._time}')
    
    def __repr__(self):
        # This method returns a string representation of the task.
        return (f'{self._description} - Due: {self._date} at {self._time}')
    
    def __lt__(self,other):
        # This method compares two tasks based on their date and time.
        month, day, year  = map(int,self._date.strip().split('/'))
        hour, min = map(int, self._time.strip().split(':'))

        other_month, other_day, other_year = map(int,other._date.strip().split('/'))
        other_hour, other_min = map(int, other._time.strip().split(':'))
        return (year, month, day, hour, min, self._description) < (other_year, other_month, other_day, other_hour, other_min, other._description)
            
