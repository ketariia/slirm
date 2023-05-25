class Dwarf:
    def accept(self, visitor):
        visitor.visit_dwarf(self)

class Elf:
    def accept(self, visitor):
        visitor.visit_elf(self)

class Troll:
    def accept(self, visitor):
        visitor.visit_troll(self)

class Project:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def interact(self, visitor):
        for employee in self.employees:
            employee.accept(visitor)

class Visitor:
    def visit_dwarf(self, dwarf):
        print("Dwarf is working on an engineering project.")

    def visit_elf(self, elf):
        print("Elf is working on a marketing project.")

    def visit_troll(self, troll):
        print("Troll is working on a management project.")

dwarf = Dwarf()
elf = Elf()
troll = Troll()

project = Project()

project.add_employee(dwarf)
project.add_employee(elf)
project.add_employee(troll)

visitor = Visitor()

project.interact(visitor)
