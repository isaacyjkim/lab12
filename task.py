class Task:
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date
        self._time = time
    
    def __str__(self):
        return (f'{self._description} - Due: {self._date} at {self._time}')
    
    def __repr__(self):
        return (f'{self._description} - Due: {self._date} at {self._time}')
    
    def __lt__(self,other):
        month, day, year  = map(int,self._date.strip().split('/'))
        hour, min = map(int, self._time.strip().split(':'))

        other_month, other_day, other_year = map(int,other._date.strip().split('/'))
        other_hour, other_min = map(int, other._time.strip().split(':'))
        return (year, month, day, hour, min, self._description) < (other_year, other_month, other_day, other_hour, other_min, other._description)
            
