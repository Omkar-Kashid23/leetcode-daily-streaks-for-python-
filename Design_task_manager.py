class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []
        self.valid = {}

        for user, task, priority in tasks:
            t = (-priority, -task, user)
            self.tasks.append(t)
            self.valid[-task] = t
        
        heapify(self.tasks)
       

    def add(self, userId: int, taskId: int, priority: int) -> None:
        t = (-priority, -taskId, userId)
        self.valid[-taskId] = t
        heappush(self.tasks, t)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        old_pri, old_task, old_user = self.valid[-taskId]
        t = (-newPriority, old_task, old_user)
        self.valid[-taskId] = t
        heappush(self.tasks, t)

    def rmv(self, taskId: int) -> None:
        del self.valid[-taskId]

    def execTop(self) -> int:
        while self.tasks:
            pri, tsk, usr = heappop(self.tasks)

            if tsk not in self.valid:
                continue
            
           
            if self.valid[tsk][0] != pri or self.valid[tsk][2] != usr:
                continue
            
            del self.valid[tsk]
            return usr
            
        return -1
