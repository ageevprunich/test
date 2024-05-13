from abc import ABC, abstractmethod

# Абстрактний клас на якому базуються всі інші
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

# Працівник на ставці
class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Працівник на % від продажів
class CommissionEmployee(Employee):
    def __init__(self, name, sales, commission):
        super().__init__(name)
        self.sales = sales
        self.commission = commission

    def calculate_salary(self):
        return self.sales * self.commission

class SalaryCommissionEmployee(Employee):
    def __init__(self, name, base_salary, sales, commission):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales = sales
        self.commission = commission

    def calculate_salary(self):
        
        return self.base_salary + self.sales * self.commission

class Container:
    def __init__(self):
        self.employees = []
    
    def __iter__(self):
        return iter(self.employees)
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        # Пошук працівника з заданим ім'ям та його видалення
        self.employees = [employee for employee in self.employees if employee.name != name]
        print(f'Employee named {name} has been removed from the container.')

    def calculate_salaries(self):
        for employee in self.employees:
            print(f'{employee.name}: {employee.calculate_salary()}')

# Створення об'єктів
cont = Container()
cont.add_employee(SalaryEmployee("John", 3000))
cont.add_employee(SalaryEmployee("Drake", 5000))
cont.add_employee(CommissionEmployee("Bob", 50000, 0.1))
cont.add_employee(CommissionEmployee("Alex", 120000, 0.1))
cont.add_employee(SalaryCommissionEmployee("Carol", 1000, 20000, 0.05))
cont.add_employee(SalaryCommissionEmployee("Kate", 2000, 10000, 0.04))

# Нарахування заробітної плати
cont.calculate_salaries()
# Видалення персоналу
cont.remove_employee("Bob")
cont.remove_employee("Kate")
cont.calculate_salaries()