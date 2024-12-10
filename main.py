import authentication as authentication
import employee_data as ed
import operations as op
import os


print("Welcome to the Employee Management System")
print("please login to continue")
auth=authentication.login()

if auth:
    while True:
        os.system('cls')
        op.options()
        choice=int(input("Enter your Choice"))
        if choice == 1:
            ed.add_employee()
        elif choice == 2:
            ed.remove_employee()
        elif choice == 3:
            ed.update_employee()
        elif choice == 4:
            op.display_info()
        elif choice == 5:
            op.calculate_bonus()
        elif choice == 6:
            op.calculate_discount()
        elif choice == 7 :
            op.Remind_legal_holidays()
        elif choice == 8 :
            op.exit()
        else:
            print("Wrong Choice, Please try Again! ")
        input("Press Enter to return to the main Menu")
        
        
        
        

