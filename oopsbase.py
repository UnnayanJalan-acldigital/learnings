class Employee:
    def __init__(self, f_name, l_name,contact):
        self.f_name = f_name
        self.l_name = l_name
        self.contact = contact

    def display_info(self):
        print(f"First Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"Contact Number: {self.contact}")
        

class Manager(Employee):
    def __init__(self, f_name, l_name, contact, department):
        super().__init__(f_name, l_name, contact)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("--" * 20)
        

class Intern(Employee):
    def __init__(self, f_name, l_name, contact, collage):
        super().__init__(f_name, l_name, contact)
        self.collage = collage
        
    def display_info(self):
        super().display_info()
        print(f"Collage: {self.collage}")
        print("--" * 20)
        

employee_list = []

def add_employee():
    employee_type=input("Enter the Employee Type(1.Regular Employee, 2.Manager, 3.Intern):")
    f_name=input("Enter the Employee's First Name:")
    l_name=input("Enter the Employee's Last Name:")
    contact=int(input("Enter the Employee's Contact Number:"))
    if employee_type=="1":
        employee=Employee(f_name,l_name,contact)
    elif employee_type=="2":
        departant=input("Enter The Manager's Departant: ")
        employee=Manager(f_name,l_name,contact,departant)
    elif employee_type=="3":
        collage=input("Enter The Intern's Collage: ")
        employee=Intern(f_name,l_name,contact,collage)
    else:
        print("Invalid Employee Type")
        return
    
    employee_list.append(employee)
    print("Employee Added Successfully\n")

def get_perticular_employee():
    contact=int(input("Enter the contact of the Employee to Get Details:"))
    for employee in employee_list:
        if employee.contact==contact:
            print("--" * 20)
            employee.display_info()
            print("--" * 20)
            return 
    print(f"Employee with contact number {contact} not found\n")


def display_all_employee():
    if not employee_list:
        print("No Employees in the list\n")
    else:
        print("\nEmployee Details:\n")
        for employee in employee_list:
            employee.display_info()

def delete_employees():
    contact=int(input("Enter the contact of the Employee to Delete:"))
    for employee in employee_list:
        if employee.contact==contact:
            employee_list.remove(employee)
            print(f"Employee whith the contact number{contact} has been deleted Successfully\n ")
            return
    print(f"Employee with contact number {contact} not found\n")

while True:
      print("1.Add Employee")
      print("2.Display All Employees")
      print("3.Delete Employee")
      print("4.To Get Pirticular user")
      print("5.To Exit")
      choice=int(input("Enter your choice"))
      
      if choice==1:
          add_employee()
      elif choice==2:
          display_all_employee()
      elif choice==3:
          delete_employees()
      elif choice==4:
          get_perticular_employee()
      elif choice==5:
        print("Exiting...")
        break
      else:
        print("Invalid choice!")
        continue
      
            