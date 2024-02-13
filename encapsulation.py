# Encapsulation
class Employee:

    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    def show(self):
        print("Name: ", self.name, 'Salary:', self.salary)

    def work(self):
        print(self.name, 'is working on', self.project)

emp = Employee('Jessica', 8000, 'NLP')

emp.show()
emp.work()