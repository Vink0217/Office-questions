'''
Q17) Employee Management 
Store employee details using classes and show details of employees in a specific department. 
'''
class Employee:
    def __init__(self,employee_id, name, department, position):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position

    def __str__(self):
        return f"[{self.employee_id}] {self.name} - {self.position} ({self.department})"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees_by_department(self, department):
        print(f"\nEmployees in '{department}' Department:")
        found = False
        for emp in self.employees:
            if emp.department.lower() == department.lower():
                print(emp)
                found = True
        if not found:
            print(f"No employees found in the '{department}' department.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee(Employee(1, "Vinayak", "HR", "Manager"))
    manager.add_employee(Employee(2, "Ahmed", "Engineering", "Software Engineer"))
    manager.show_employees_by_department("HR")

