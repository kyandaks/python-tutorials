class Employee:

    def __init__(self, name, salary, duration):
        self.name = name
        self.salary = salary
        self.duration = duration


    def time_spent(self):
        return self.salary * self.duration

kyanda = Employee('kyanda', 1000, 10)
print(f'Employee name: {kyanda.name}')
print(f'Salary: {kyanda.salary}')
print(f'time spent at work: {kyanda.duration}')
print(kyanda.time_spent())

# instance level attributes
# class level attributes
# @classmethods
# @staticmethods