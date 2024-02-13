class Employee:
    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com".lower()
        Employee.num_of_emp += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def appply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")


dev_1 = Developer("Yeabsera", "Lisanework", 6000, "Python")
dev_2 = Developer("Casper", "Gost", 6000, "JS")

mgr_1 = Manager("Abel", "Josh", 3000, [dev_1])

mgr_1.add_emp(dev_2)

print(mgr_1.print_emp())

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Developer))
