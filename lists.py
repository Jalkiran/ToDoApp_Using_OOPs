from tasks import Task
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        title=input('Title:')
        t=Task(title)
        self.tasks.append(t)
        print('Task Added Successfully!')
    def show_tasks(self):
        if not self.tasks:
            print('No Tasks Yet!')
            return
        else:
            for i,t in enumerate(self.tasks,1):
                status='✓'if t.completed_status else'✕'
                print(f'{i}.[{status}]{t.title}')
    def status(self):
        found=False
        title=input('Enter task:')
        for t in self.tasks:
            if t.title==title:
                t.completed_status=True
                print('Task marked as completed!')
                found=True
                break
        if not found:
            print('Task Not Found')
    
