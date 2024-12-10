import employee_data as ed
import sys
def display_info():
    id=int(input("Enter Employee ID: "))
    for i in range(len(ed.Employee_list)):
        if ed.Employee_list[i].get("ID") == id:
            print("Employee Information")
            print("Employee Name: ",ed.Employee_list[i].get("Name"))
            print("Employee Department: ",ed.Employee_list[i].get("Department"))
            print("Employee Salary: ",ed.Employee_list[i].get("Salary"))
            print("Employee absence days: ",ed.Employee_list[i].get("absence_days"))
            break
    else:
        print(".. Employee not Found ..")

def calculate_bonus():
    id=int(input("Enter Employee ID: "))
    for i in range(len(ed.Employee_list)):
        if ed.Employee_list[i].get("ID") == id:
            bonus=ed.Employee_list[i].get("Salary")*0.1
            print("Bonus Calculation")
            print("Bonus: ",bonus)
            break
    else:
        print(".. Employee not Found ..")

def calculate_discount():
    id=int(input("Enter Employee ID: "))
    for i in range(len(ed.Employee_list)):
        if ed.Employee_list[i].get("ID") == id:
            discount=ed.Employee_list[i].get("Salary")*0.05
            print("Discount Calculation")
            print("Discount: ",discount)
            break
    else:
        print(".. Employee not Found ..")

def Remind_legal_holidays():
    id=int(input("Enter Employee ID: "))
    for i in range(len(ed.Employee_list)):
        if ed.Employee_list[i].get("ID") == id:
            legal_holidays=10-(ed.Employee_list[i].get("absence_days"))
            print("Reminder")
            print("Remaining Legal Holidays: ",legal_holidays)
            break
    else:
        print(".. Employee not Found ..")

def exit():
    sys.exit("Thank you for using the Employee Management System. Goodbye!")

def options():
    print("Select an option")
    print("1. Add Employee Information")
    print("2. Remove Employee Information")
    print("3. Update Employee Information")
    print("4. Display Employee Information")
    print("5. Calculate Bonus")
    print("6. Calculate Discount")
    print("7. Remind Legal Holidays")
    print("8. Exit")