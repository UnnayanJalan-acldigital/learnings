class Employee:
    def __init__(self, f_name, l_name,contact):
        self.f_name = f_name
        self.l_name = l_name
        self.contact = contact

    def display_info(self):
        print(f"First Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"Contact Number: {self.contact}")
        print("--" * 20)

employees_list=[]

def add_employee():
    f_name=input("Enter the Employee's First Name:")
    l_name=input("Enter the Employee's Last Name:")
    contact=int(input("Enter the Employee's Contact Number:"))

    employees=Employee(f_name,l_name,contact)
    employees_list.append(employees)
    print("\nEmployee added successfully")
    for employee in employees_list:
            employee.display_info()
    
    
    
def display_all_employees():
    if not employees_list:
        print("No employees in the list\n")
    else:
        print("Employee Details:")
        for employee in employees_list:
            employee.display_info()

def delete_employees():
    contact=int(input("Enter the contact of the Employee to Delete:"))
    for employee in employees_list:
        if employee.contact==contact:
            employees_list.remove(employee)
            print(f"Employee whith th contact number{contact} has been deleted Successfully\n ")
            return
    print(f"Employee with contact number {contact} not found")
            
        
while True:
    print("1.Add Employee")
    print("2.Display All Employees")
    print("3.Delete Employee")
    print("4.To Exit")
    choice=int(input("Enter your choice"))

    if choice==1:
        add_employee()
    elif choice==2:
        display_all_employees()
    elif choice==3:
        delete_employees()
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
        continue
    



