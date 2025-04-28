
class Tasklist: 


    def __init__(self):
        self._tasks = [] 
        self._n = 0
        with open('tasklist-1.txt', 'r') as f: 
            for line in f: 
                task = line.strip('\n').split(',')
                self._tasks.append(task) 
        f.close()


    def add_task(self, desc, date, time): 
        pass 


    def get_current_task(self): 
        pass 

    
    def mark_complete(self): 
        pass 

    def save_file(self): 
        pass 

    def __len__(self): 
        pass 

    def __iter__(self): 
        pass 

    def __next__(self): 
        pass 
        

    # Test  method
    def __str__(self): 
        return str(self._tasks)
