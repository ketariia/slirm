import json

class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.amount}: {self.description}"

    def __del__(self):
        print(f"Transaction {self.amount} deleted.")

class Department:
    def __init__(self, name, faculty, head, number, floor, phone_number, student_capacity):
        self.name = name
        self.faculty = faculty
        self.head = head
        self.number = number
        self.floor = floor
        self.phone_number = phone_number
        self.student_capacity = student_capacity
        self.disciplines = []
        self.transactions = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def add_transaction(self, amount, description):
        self.transactions.append(Transaction(amount, description))

    def to_dict(self):
        return {
            "name": self.name,
            "faculty": self.faculty,
            "head": self.head,
            "number": self.number,
            "floor": self.floor,
            "phone_number": self.phone_number,
            "student_capacity": self.student_capacity,
            "disciplines": [d.name for d in self.disciplines],
            "transactions": [t.__dict__ for t in self.transactions],
        }

    def from_dict(self, data, disciplines):
        self.name = data["name"]
        self.faculty = data["faculty"]
        self.head = data["head"]
        self.number = data["number"]
        self.floor = data["floor"]
        self.phone_number = data["phone_number"]
        self.student_capacity = data["student_capacity"]
        self.disciplines = [disciplines[d] for d in data["disciplines"]]
        self.transactions = [
            Transaction(t["amount"], t["description"]) for t in data["transactions"]
        ]

    def __str__(self):
        return f"{self.name} ({self.faculty})"

    def __del__(self):
        print(f"Department {self.name} deleted.")

class Person:
    def __init__(self, last_name, first_name, patronymic, gender, address, city, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.gender = gender
        self.address = address
        self.city = city
        self.phone_number = phone_number
        self.transactions = []

    def add_transaction(self, amount, description):
        self.transactions.append(Transaction(amount, description))

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __del__(self):
        print(f"{self.__class__.__name__} {self.last_name} {self.first_name} deleted.")

class Teacher(Person):
    def __init__(self, last_name, first_name, patronymic, department, birth_year, employment_year, experience, position, gender, address, city, phone_number):
        super().__init__(last_name, first_name, patronymic, gender, address, city, phone_number)
        self.department = department
        self.birth_year = birth_year
        self.employment_year = employment_year
        self.experience = experience
        self.position = position
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "department": self.department.name,
            "birth_year": self.birth_year,
            "employment_year": self.employment_year,
            "experience": self.experience,
            "position": self.position,
            "gender": self.gender,
            "address": self.address,
            "city": self.city,
            "phone_number": self.phone_number,
            "disciplines": [d.name for d in self.disciplines],
            "transactions": [t.__dict__ for t in self.transactions],
        }

    def from_dict(self, data, departments, disciplines):
        super().from_dict(data, departments, disciplines)
        self.department = departments[data["department"]]
        self.birth_year = data["birth_year"]
        self.employment_year = data["employment_year"]
        self.experience = data["experience"]
        self.position = data["position"]
        self.disciplines = [disciplines[d] for d in data["disciplines"]]

class Student(Person):
    def __init__(self, last_name, first_name, patronymic, department, birth_year, gender, address, city, phone_number):
        super().__init__(last_name, first_name, patronymic, gender, address, city, phone_number)
        self.department = department
        self.birth_year = birth_year
        self.academic_performances = []

    def add_academic_performance(self, academic_performance):
        self.academic_performances.append(academic_performance)
        self.transactions.append(Transaction(0, "New academic performance added."))

    def get_academic_performance(self, discipline):
        for academic_performance in self.academic_performances:
            if academic_performance.discipline == discipline:
                return academic_performance.grade
        return None

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "department": self.department.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "address": self.address,
            "city": self.city,
            "phone_number": self.phone_number,
            "academic_performances": [
                {
                    "discipline": ap.discipline.name,
                    "teacher": ap.teacher.last_name + " " + ap.teacher.first_name,
                    "grade": ap.grade,
                }
                for ap in self.academic_performances
            ],
            "transactions": [t.__dict__ for t in self.transactions],
        }

    def from_dict(self, data, departments, disciplines, teachers):
        super().from_dict(data, departments, disciplines, teachers)
        self.department = departments[data["department"]]
        self.birth_year = data["birth_year"]
        self.academic_performances = [
            AcademicPerformance(teachers[ap["teacher"]], disciplines[ap["discipline"]], self, ap["grade"])
            for ap in data["academic_performances"]
        ]

class AcademicPerformance:
    def __init__(self, teacher, discipline, student, grade):
        self.teacher = teacher
        self.discipline = discipline
        self.student = student
        self.grade = grade
        self.transactions = []

    def add_transaction(self, amount, description):
        self.transactions.append(Transaction(amount, description))

    def to_dict(self):
        return {
            "teacher": self.teacher.last_name + " " + self.teacher.first_name,
            "discipline": self.discipline.name,
            "student": self.student.last_name + " " + self.student.first_name,
            "grade": self.grade,
            "transactions": [t.__dict__ for t in self.transactions],
        }

    def from_dict(self, data, teachers, disciplines, students):
        self.teacher = teachers[data["teacher"]]
        self.discipline = disciplines[data["discipline"]]
        self.student = students[data["student"]]
        self.grade = data["grade"]
        self.transactions = [
            Transaction(t["amount"], t["description"]) for t in data["transactions"]
        ]

    def __str__(self):
        return f"{self.grade} ({self.teacher}, {self.discipline}, {self.student})"

    def __del__(self):
        print(f"AcademicPerformance {self.grade} deleted.")

class Discipline:
    def __init__(self, name, department, teacher, hours, exam_type):
        self.name = name
        self.department = department
        self.teacher = teacher
        self.hours = hours
        self.exam_type = exam_type
        self.academic_performances = []
        self.transactions = []

    def add_academic_performance(self, academic_performance):
        self.academic_performances.append(academic_performance)
        self.transactions.append(Transaction(0, "New academic performance added."))

    def add_transaction(self, amount, description):
        self.transactions.append(Transaction(amount, description))

    def to_dict(self):
        return {
            "name": self.name,
            "department": self.department.name,
            "teacher": self.teacher.last_name + " " + self.teacher.first_name,
            "hours": self.hours,
            "exam_type": self.exam_type,
            "academic_performances": [
                {
                    "student": ap.student.last_name + " " + ap.student.first_name,
                    "grade": ap.grade,
                }
                for ap in self.academic_performances
            ],
            "transactions": [t.__dict__ for t in self.transactions],
        }

    def from_dict(self, data, departments, teachers, students):
        self.name = data["name"]
        self.department = departments[data["department"]]
        self.teacher = teachers[data["teacher"]]
        self.hours = data["hours"]
        self.exam_type = data["exam_type"]
        self.academic_performances = [
            AcademicPerformance(
                self.teacher, self, students[ap["student"]], ap["grade"]
            )
            for ap in data["academic_performances"]
        ]
        self.transactions = [
            Transaction(t["amount"], t["description"]) for t in data["transactions"]
        ]

    def __str__(self):
        return f"{self.name} ({self.department})"

    def __del__(self):
        print(f"Discipline {self.name} deleted.")
