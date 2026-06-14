**Python To-Do List App 📝**
  A simple command-line To-Do List application built using Python. This project allows users to add tasks, view all tasks, mark tasks as completed, and delete tasks from the list.

**📌 Features**
 1 Add a new task
 2 View all tasks
 3 Mark a task as completed
 4 Delete an existing task
 5 Shows task status using symbols:
    ✓ = Completed
    ✕ = Not Completed
  Simple and beginner-friendly Python project
  
**🛠️ Tech Stack**
    Python
    Object-Oriented Programming concepts
    
**📂 Project Structure**
    To-Do-List/
    │
    ├── main.py
    ├── todo_list.py
    ├── tasks.py
    └── README.md
    
**📄 File Description**
   1) tasks.py
      ->This file contains the Task class, which stores the task title and completion status.
      Example:
      
          class Task:
              def __init__(self, title):
                  self.title = title
                  self.completed_status = False
   2) todo_list.py
      ->This file contains the ToDoList class. It manages all task-related operations like adding, showing, completing, and deleting tasks.

        Main functions:
        
        add_task() - Adds a new task
        show_tasks() - Displays all tasks
        status() - Marks a task as completed
        delete_task() - Deletes a task
    3) main.py
      ->This file can be used to run the application and display the menu to the user.

        Example:
                from todo_list import ToDoList
                
                app = ToDoList()
                
                while True:
                    print("1. Add Task")
                    print("2. Show Tasks")
                    print("3. Mark Task as Completed")
                    print("4. Delete Task")
                    print("5. Exit")
                
                    choice = input("Enter your choice: ")
                
                    if choice == "1":
                        app.add_task()
                    elif choice == "2":
                        app.show_tasks()
                    elif choice == "3":
                        app.status()
                    elif choice == "4":
                        app.delete_task()
                    elif choice == "5":
                        print("Exiting To-Do List App...")
                        break
                    else:
                        print("Invalid choice! Please try again.\n")
**🚀 How to Run the Project**
    1. Clone the repository:
        git clone https://github.com/your-username/to-do-list-python.git
    2. Open the project folder:
        cd to-do-list-python
    3. Run the Python file:
        python main.py
        
**📖 How to Use**
      1.  Run the program.
      2.  Choose an option from the menu.
      3.  Add a task by entering its title.
      4.  View all tasks using the show option.
      5.  Mark a task as completed by entering its title.
      6.  Delete a task by entering its title.
      7.  Exit the program when finished.
      
**✅ Sample Output**

        1. Add Task
        2. Show Tasks
        3. Mark Task as Completed
        4. Delete Task
        5. Exit
        
        Enter your choice: 1
        Title: study python
        ----Task Added Successfully!----
        
        Enter your choice: 2
        ----To Do List----
        
        1.[✕]Study Python
        
**🎯 Concepts Used**
      1  Classes and Objects
      2  Lists
      3  Loops
      4  Conditional Statements
      5  User Input
      6  String Methods
      7  Object-Oriented Programming
  
**⚠️ Important Note**
    In Python, the constructor should be written as:
        def __init__(self):
    Not as:
        def **init**(self):
So make sure your code uses double underscores before and after init.

**🔮 Future Improvements**
     1 Save tasks permanently using a file
     2 Add due dates for tasks
     3 Add task priority
     4 Edit existing tasks
     5 Add search functionality
     6 Add a graphical user interface
     
**🙋‍♀️ Author**
    Jalkiran Kaur
    
    GitHub: Jalkiran

**📄 License**
    This project is open-source and available under the MIT License.
