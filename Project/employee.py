#Nader John

from person import Person

class Employee(Person):
    def __init__(self, name, money, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "lazy"
        else:
            self.mood = "tired"

    def drive(self):
        self.car.run(self.distanceToWork, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)

    def send_mail(self, to, subject, body):
        print(f"Sending mail to: {to}\nSubject: {subject}\nBody: {body}")
