from task import Task

class Tasklist: 

    """
    A class to represent a list of tasks.
    """
    def __init__(self):
        # This method initializes the task list and loads tasks from a file.
        self._tasks = [] 
        with open('tasklist-1.txt', 'r') as f: 
            for line in f: 
                tasks = line.strip('\n').split(',')
                self._tasks.append(Task(tasks[0], tasks[1], tasks[2])) 
        self._tasks.sort()
        self.save_file()
        f.close()


    def add_task(self, desc, date, time): 
        # This method adds a new task to the task list.
        # It takes a description, date, and time as input.
        self._tasks.append(Task(desc, date, time)) 
        self._tasks.sort()
        self.save_file() 

        

    def get_current_task(self): 
        # This method returns the current task in the task list.
        # It returns None if there are no tasks.
        return self._tasks[0] if self._tasks else None
    
    def mark_complete(self): 
        # This method marks the current task as complete by removing it from the task list.
        # It also saves the updated task list to a file.
        if self._tasks: 
            self._tasks.pop(0) 
        self.save_file()

    def save_file(self): 
        # This method saves the current task list to a file.
        with open('tasklist-1.txt', 'w') as f:
            for task in self._tasks: 
                f.write(f'{task._description},{task._date},{task._time}\n') 

    def __len__(self): 
        # This method returns the number of tasks in the task list.
        return len(self._tasks)

    def __iter__(self): 
        # This method returns an iterator for the task list.
        self._n = 0 
        return self

    def __next__(self): 
        # This method returns the next task in the task list.
        # It raises StopIteration when there are no more tasks.
        if self._n < len(self._tasks): 
            task = self._tasks[self._n]
            self._n += 1 
            return task
        else: 
            raise StopIteration
        

    # Test  method 
    # This method returns a string representation of the task list.
    def __str__(self): 
        return str(self._tasks)
