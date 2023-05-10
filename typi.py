from typing import TypeVar

from disp import Discipline, Teacher

T = TypeVar('T', bound=Discipline)

class Department:
    def __init__(self, name: str, faculty: str, head: str, number: int, floor: int, phone_number: str, student_capacity: int):
        self.name = name
        self.faculty = faculty
        self.head = head
        self.number = number
        self.floor = floor
        self.phone_number = phone_number
        self.student_capacity = student_capacity
        self.disciplines: list[T] = []

    def add_discipline(self, discipline: T, teacher: Teacher = None):
        self.disciplines.append(discipline)
        discipline.department = self
        if teacher:
            self.add_teacher(teacher)

    def add_teacher(self, teacher: Teacher):
        teacher.department = self

    def __str__(self):
        return self.name
department = Department[Discipline]("Кафедра математики", "Факультет естественных наук", "Александрович Иван Алексеев", 101, 2, "+7 (999) 999-99-99", 10)
teacher1 = Teacher("Барболина", "Екатерина", "Сергеевна", department, 1980, 2005, 15, "старший преподаватель", "женский", "ул. Пушкина, д. 10, кв. 5", "Москва", "+7 (999) 888-88-88")
discipline1 = Discipline("Математический анализ", department, teacher1, 120, "Written Exam")

department.add_discipline(discipline1, teacher1)
   