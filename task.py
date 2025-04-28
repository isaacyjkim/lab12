class Task:
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date
        self._time = time
    
    def __str__(self):
        return (f'{self._description} - Due: {self._date} at{self._time}')
    
    def __repr__(self):
        return (f'{self._description} - Due: {self._date} at {self._time}')
    
    def __lt__(self,other):
        year, month, day = self._date.strip().split('/')
        hour, min = self._time.strip().split(':')

        other_year, other_month, other_day = other._date.strip().split('/')
        other_hour, other_min = other._time.strip().split(':')
        return (year, month, day, hour, min, self._description) < (other_year, other_month, other_day, other_hour, other_min, other._description)
            
