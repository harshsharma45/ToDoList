#To_Do_List using Python

def main():
    my_tasks = [ ]
    print("To-Do List")
    print("welcome to your Daily Routine Tracker List \nEnter your choice")
    try:
        while True:
            print("1.Add Task")
            print("2.Remove Task")
            print("3.View Task")
            print("4.Quit")

            choice = int(input("Enter your choice:"))

            if choice==1:
                print("Add Task")
                n = int(input("enter the number of tasks:"))
                for i in range(n):
                    lis_input = input("Enter the tasks to add:")
                    my_tasks.append(lis_input)
                print("Your Tasks =",my_tasks)

            elif choice == 2:
                if len(my_tasks)==0:
                    print("You have no task to remove.")

                elif len(my_tasks) >=1:
                    print("Task to remove")
                    lis_op = input("Enter the task to remove:")
                    if lis_op in my_tasks:
                        my_tasks.remove(lis_op)
                    else:
                        print("Task is not in list.")
                    print("Remaining Tasks =",my_tasks)

            elif choice ==3:
                if len(my_tasks) == 0:
                    print("You have no task to view.",my_tasks)
                elif len(my_tasks) >= 1:
                    print("Your added tasks = ",my_tasks)

            elif choice ==4:
                print("Thank you for using this program.")
                break

            else:
                print("Invalid Choice")
                print("Enter the choice Again:")

    except ValueError:
        print("Please enter the choices from list.")



if __name__ ==  "__main__":
    main()