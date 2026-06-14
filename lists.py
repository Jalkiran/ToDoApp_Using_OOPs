from tasks import Task
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        title=input('Title:').title()
        t=Task(title)
        self.tasks.append(t)
        print('----Task Added Successfully!----\n')
    def show_tasks(self):
        if not self.tasks:
            print('----No Tasks Yet!----\n')
            return
        else:
            print('----To Do List----\n')
            for i,t in enumerate(self.tasks,1):
                status='✓'if t.completed_status else'✕'
                print(f'{i}.[{status}]{t.title}')
            print()
    def status(self):
        found=False
        title=input('Title:').title()
        for t in self.tasks:
            if t.title==title:
                t.completed_status=True
                print('----Task marked as completed!----\n')
                found=True
                break
        if not found:
            print('----Task Not Found----\n')
    def delete_task(self):
        title=input('Title:').title()
        found=False
        for t in self.tasks:
            if t.title==title:
                self.tasks.remove(t)
                found=True
                print('----Task Deleted Successfully!----\n')
                break
        if not found:
            print('----Task does not exist!----\n')
