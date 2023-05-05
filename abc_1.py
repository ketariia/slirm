from abc import ABC, abstractmethod
from dataclasses import dataclass

class Performance(ABC):
    @abstractmethod
    def get_grade(self):
        pass

class AcademicPerformance(Performance):
    def __init__(self, teacher, discipline, student, grade):
        self.teacher = teacher
        self.discipline = discipline
        self.student = student
        self.grade = grade

    def get_grade(self):
        return self.grade

class Person(ABC):
    @abstractmethod
    def get_last_name(self):
        pass

    @abstractmethod
    def get_first_name(self):
        pass

    @abstractmethod
    def get_patronymic(self):
        pass

    @abstractmethod
    def get_department(self):
        pass

    @abstractmethod
    def get_birth_year(self):
        pass

    @abstractmethod
    def get_gender(self):
        pass

    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def get_city(self):
        pass

    @abstractmethod
    def get_phone_number(self):
        pass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    gender: str

class Teacher(Person):
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

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_patronymic(self):
        return self.patronymic

    def get_department(self):
        return self.department

    def get_birth_year(self):
        return self.birth_year

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_phone_number(self):
        return self.phone_number

class Student(Person):
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

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_patronymic(self):
        return self.patronymic

    def get_department(self):
        return self.department

    def get_birth_year(self):
        return self.birth_year

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_phone_number(self):
        return self.phone_number

class AcademicObject(ABC):
    @abstractmethod
    def add_academic_performance(self, performance):
        pass

    @abstractmethod
    def add_discipline(self, discipline):
        pass

class Department(AcademicObject):
    def __init__(self, name, faculty, head, number, floor, phone_number, student_capacity):
        self.name = name
        self.faculty = faculty
        self.head = head
        self.number = number
        self.floor = floor
        self.phone_number = phone_number
        self.student_capacity = student_capacity
        self.disciplines = []

    def add_academic_performance(self, performance):
        for discipline in self.disciplines:
            if discipline.name == performance.discipline.name:
                discipline.add_academic_performance(performance)

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)
        discipline.department = self

class Teacher(AcademicObject):
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

    def add_academic_performance(self, performance):
        for discipline in self.disciplines:
            if discipline.name == performance.discipline.name:
                discipline.add_academic_performance(performance)

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)
        discipline.teacher = self
person1 = Person("Кай", "Барболин", 18, "male")
person2 = Person("Катя", "Барболина", 18, "female")

   