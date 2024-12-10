import getpass

Employee_list=[{ "ID":101,"Name":"Habeba",
                "Department":"Engineering",
                "Salary":10000,
                "password":1020,
                "absence_days":2}]

def add_employee():
    print(".. Enter Employee Information ..")
    id=int(input("Enter the Employee ID: "))
    if(check_duplicate(id)):
        print(".. ID already exists ..")
    else:       
        temp_dict={"ID":id,
                "Name":input("Enter the Employee Name "),
                "Department":input("Enter the Employee Department "),
                "Salary":int(input("Enter the Employee Salary ")),
                "password":int(getpass.getpass("Enter the Employee password ")),
                "absence_days":int(input("Enter the Employee absence days "))}
        Employee_list.append(temp_dict)
        print(".. Employee is added successfully ..")

def remove_employee():
    print(".. Enter the Employee Information to be removed ..")
    id=int(input("Enter the employee ID: "))
    for i in range(len(Employee_list)):
        if Employee_list[i].get("ID") == id:
            del Employee_list[i]
            print(".. Employee is removed Successfully ..")
            break
    else:
        print(".. Employee ID is not found ..")


def update_employee():
    print(".. Enter Employee Information to be updated ..")
    id=int(input("Enter the employee ID: "))
    for i in range(len(Employee_list)):
        if Employee_list[i].get("ID") == id:
            Employee_list[i].update({"Name":input("Enter the Employee Name ")})
            Employee_list[i].update({"Department":input("Enter the Employee Department ")})
            Employee_list[i].update({"Salary":int(input("Enter the Employee Salary "))})
            Employee_list[i].update({"password":int(input("Enter the Employee Password "))})
            Employee_list[i].update({"absence_days":int(input("Enter the Employee absence days "))})
            print(".. Employee is updated Successfully ..")
            break
    else:
        print("Employee ID is not found")

def check_duplicate(id):
    for i in range(len(Employee_list)):
        if Employee_list[i].get("ID") == id:
            return 1 
        