from tasks import Task
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_tasks(self):
        title=input('Title:')
        completed_status=input('Complete Status:')
        t=Task(title)
        self.tasks.append(t)
        print('Task Added Successfully!')

        