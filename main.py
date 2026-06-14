from lists import ToDoList
tdl=ToDoList()
while True:
    print('\n---Menu---')
    print('1.Add Task')
    print('2.View Tasks')
    print('3.Mark Status')
    print('4.Delete Task')
    print('5.Exit\n')

    choice=int(input('Enter Your Choice:'))
    if choice==1:
        tdl.add_task()
    elif choice==2:
        tdl.show_tasks()
    elif choice==3:
        tdl.status()
    elif choice==4:
        tdl.delete_task()
    elif choice==5:
        print('Goodbye!')
        break
    else:
        print('\n----Invalid Input----\n')