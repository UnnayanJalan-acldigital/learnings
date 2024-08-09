class employee_detils:
    def __init__(self):
        self.name = input("Enter the Employee Name: ")
        self.roll_no = int(input("Enter the Employee Roll no.: "))
        self.contact = int(input("Enter the Employee Contact Details: "))

    def show_details(self):
        print(f"Employee Name is {self.name}")
        print(f"Employee Roll no. is {self.roll_no}")
        print(f"Employee Contact Details is {self.contact}")

employee=employee_detils()
employee.show_details()

