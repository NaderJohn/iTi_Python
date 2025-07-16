#Nader John

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if not employee:
            return

        # Calculate arrival time
        if employee.car.velocity == 0:  # Prevent division by zero
            travel_time = float('inf')
        else:
            travel_time = employee.distanceToWork / employee.car.velocity  # in hours
        
        arrival_time = moveHour + travel_time

        # Check if late (arrival after 9 AM)
        if arrival_time > 9.0:
            deduction = employee.salary * 0.1  # Deduct 10%
            self.deduct(empId, deduction)
            print(f"{employee.name} was late! Salary reduced by 10%.")
        else:
            print(f"{employee.name} arrived on time.")

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num