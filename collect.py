from collections import namedtuple

AcademicPerformance = namedtuple("AcademicPerformance", ["teacher", "discipline", "student", "grade"])

class Discipline:
    def __init__(self, name, department, teacher, hours, exam_type):
        self.name = name
        self.department = department
        self.teacher = teacher
        self.hours = hours
        self.exam_type = exam_type
        self.academic_performances = []

    def add_academic_performance(self, performance):
        self.academic_performances.append(performance)

    def __str__(self):
        return self.name

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

    def add_discipline(self, discipline, teacher=None):
        self.disciplines.append(discipline)
        discipline.department = self
        if teacher:
            self.add_teacher(teacher)

    def add_teacher(self, teacher):
        teacher.department = self

    def __str__(self):
        return self.name

class Teacher:
    def __init__(self, last_name, first_name, patronymic, department, birth_year, employment_year, experience, position, gender, address, city, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.department = department
        self.birth_year = birth_year
        self.employment_year = employment_year
        self.experience = experience
        self.position = position
        self.gender = gender
        self.address = address
        self.city = city
        self.phone_number = phone_number
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)
        discipline.teacher = self

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

class Student:
    def __init__(self, last_name, first_name, patronymic, department, birth_year, gender, address, city, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.department = department
        self.birth_year = birth_year
        self.gender = gender
        self.address = address
        self.city = city
        self.phone_number = phone_number
        self.academic_performances = []

    def add_academic_performance(self, performance, discipline):
        self.academic_performances.append(performance)
        discipline.add_academic_performance(performance)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


department = Department("Кафедра математики", "Факультет естественных наук", "Александрович Иван Алексеев", 101, 2, "+7 (999) 999-99-99", 10)
teacher1 = Teacher("Барболина", "Екатерина", "Сергеевна", department, 1980, 2005, 15, "старший преподаватель", "женский", "ул. Пушкина, д. 10, кв. 5", "Москва", "+7 (999) 888-88-88")
discipline1 = Discipline("Математический анализ", department, teacher1, 120, "Written Exam")

student1 = Student("Александрович", "Иван", "Алексеев", department, 2000, "мужской", "ул. Ленина, д. 23, кв. 12", "Москва", "+7 (999) 777-77-77")
performance1 = AcademicPerformance(teacher1, discipline1, student1, 5)

department.add_discipline(discipline1, teacher1)
student1.add_academic_performance(performance1, discipline1)

print(student1)
for performance in student1.academic_performances:
    print(performance.grade)
