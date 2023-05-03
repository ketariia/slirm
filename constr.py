from desrt import Transaction


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

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def __str__(self):
        return f"{self.name}, факультет: {self.faculty}, заведующий: {self.head}, номер кабинета: {self.number}, этаж: {self.floor}, телефон: {self.phone_number}, вместимость студентов: {self.student_capacity}"



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

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, {self.position}, {self.experience} лет опыта работы, телефон: {self.phone_number}, адрес: {self.address}, город: {self.city}"



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
        return f"{self.name}, отделение: {self.department.name}, преподаватель: {self.teacher.last_name} {self.teacher.first_name} {self.teacher.patronymic}, часы: {self.hours}, тип экзамена: {self.exam_type}"



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

    def add_academic_performance(self, performance):
        self.academic_performances.append(performance)

    def get_academic_performance(self, discipline):
        for performance in self.academic_performances:
            if performance.discipline == discipline:
                return performance.grade
        return None

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, {self.birth_year} года рождения, телефон: {self.phone_number}, адрес: {self.address}, город: {self.city}"



class AcademicPerformance:
    def __init__(self, teacher, discipline, student, grade):
        self.teacher = teacher
        self.discipline = discipline
        self.student = student
        self.grade = grade

    def __str__(self):
        return f"{self.student.last_name} {self.student.first_name} {self.student.patronymic} - {self.discipline.name}: {self.grade}"
    