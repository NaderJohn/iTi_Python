#Nader John

from car import Car
from employee import Employee
from office import Office
import re  

def main():
    print(" ITI Office Simulation")

    # === Constants from Lab Story ===
    office = Office("ITI Smart Village")
    car_name = "Fiat128"
    fuel_rate = 100
    default_velocity = 60
    default_distance_to_work = 20
    default_money = 100.0
    default_health = 100

    emp_count = int(input("How many employees do you want to add? "))

    for i in range(emp_count):
        print(f"\n Enter info for Employee {i+1}")
        name = input("Name: ")
        emp_id = int(input("Employee ID: "))

        # Email validation
        while True:
            email = input("Email: ")
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                break
            else:
                print(" Invalid email format. Please try again.")

        salary = float(input("Salary (L.E): "))
        move_hour = float(input("When did they leave home? (e.g. 7.5 = 7:30 AM): "))
        sleep_hours = float(input("How many hours did they sleep last night? "))
        work_hours = int(input("How many hours did they work today? "))
        meals = int(input("How many meals did they eat today (1–3)? "))

        # Create Car and Employee objects
        car = Car(car_name, fuel_rate, default_velocity)
        emp = Employee(name, default_money, default_health, emp_id, car, email, salary, default_distance_to_work)

        office.hire(emp)

        # Simulate employee day
        print(f"\n {name} is heading to work...")
        emp.drive()
        office.check_lateness(emp_id, move_hour)
        emp.sleep(sleep_hours)
        emp.work(work_hours)
        emp.eat(meals)
        emp.buy(1)

        # Summary
        print(f"{name}'s mood after work: {emp.mood}")
        print(f"{name}'s salary after lateness check: {emp.salary} L.E")
        print(f"{name}'s health rate after eating: {emp.healthRate}")

    print(f"\n Total Employees Hired: {Office.employeesNum}")

if __name__ == "__main__":
    main()
