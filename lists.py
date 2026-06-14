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
                print(f'{i}.{t.title}')
            