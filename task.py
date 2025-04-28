class Task:
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date
        self._time = time
    
    def __str__(self):
        return (f'{self._description} - Due: {self.date} at {self.time}')
    
    def __repr__(self):
        return (f'{self._description} - Due: {self.date} at {self.time}')
    
    def __lt__(self,other):
        year, month, day = self.date.split('/').strip()
        hour, min = self.time.split(':').strip()

        other_year, other_month, other_day = other.date.split('/').strip()
        other_hour, other_min = other.time.split(':').strip()
        return (year, month, day, hour, min, self.description) < (other_year, other_month, other_day, other_hour, other_min, other.description)
            
