from task import Task

class Tasklist: 


    def __init__(self):
        self._tasks = [] 
        with open('tasklist-1.txt', 'r') as f: 
            for line in f: 
                tasks = line.strip('\n').split(',')
                self._tasks.append(Task(tasks[0], tasks[1], tasks[2])) 
        self._tasks.sort()
        self.save_file()
        f.close()


    def add_task(self, desc, date, time): 
        self._tasks.append(Task(desc, date, time)) 
        self._tasks.sort()
        self.save_file() 

        

    def get_current_task(self): 
        return self._tasks[0] if self._tasks else None
    
    

    
    def mark_complete(self): 
        if self._tasks: 
            self._tasks.pop(0) 

        self.save_file()

    def save_file(self): 
        with open('tasklist-1.txt', 'w') as f:
            for task in self._tasks: 
                f.write(f'{task._description},{task._date},{task._time}\n') 

    def __len__(self): 
        return len(self._tasks)

    def __iter__(self): 
        self._n = 0 
        return self

    def __next__(self): 
        if self._n < len(self._tasks): 
            task = self._tasks[self._n]
            self._n += 1 
            return task
        else: 
            raise StopIteration
        

    # Test  method
    def __str__(self): 
        return str(self._tasks)
