class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{last}@company.com"


emp1 = Employee("Yeabsera", "Lisanework", 5000)
emp2 = Employee("Abel", "Alemu", 9000)

print(emp1.first)
