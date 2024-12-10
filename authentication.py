import employee_data as ed
import getpass

def login():
    for j in range(1,4):
        for i in range(len(ed.Employee_list)):
            id=int(input("Enter Employee ID: "))
            if ed.Employee_list[i].get("ID")==id:
                password =int(getpass.getpass("Enter the Employee password "))
                if ed.Employee_list[i].get("password")==password:
                    print(" Login Successful! ")
                    return 1
                else:
                    print("Login Failed, Please try again. Attempts left: ",3-j)
    return 0




    
