class Department:
    def __init__(self, name, faculty, head, room_number, building_number, phone_number, num_teachers):
        self.name = name
        self.faculty = faculty
        self.head = head
        self.room_number = room_number
        self.building_number = building_number
        self.phone_number = phone_number
        self.num_teachers = num_teachers
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

class Teacher:
    def __init__(self, last_name, first_name, patronymic, department, birth_year, start_year, experience, position, gender, address, city, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.department = department
        self.birth_year = birth_year
        self.start_year = start_year
        self.experience = experience
        self.position = position
        self.gender = gender
        self.address = address
        self.city = city
        self.phone_number = phone_number
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def get_academic_performance(self, discipline, student):
        for performance in discipline.academic_performances:
            if performance.student == student:
                return performance.grade
        return None

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

class Discipline:
    def __init__(self, name, department, teacher, hours, final_control_type):
        self.name = name
        self.department = department
        self.teacher = teacher
        self.hours = hours
        self.final_control_type = final_control_type
        self.academic_performances = []

    def add_academic_performance(self, performance):
        self.academic_performances.append(performance)

class AcademicPerformance:
    def __init__(self, teacher, discipline, student, grade):
        self.teacher = teacher
        self.discipline = discipline
        self.student = student
        self.grade = grade
        teacher.add_discipline(discipline)
        student.add_academic_performance(self)
        discipline.add_academic_performance(self)

department = Department("Кафедра математики", "Факультет естественных наук", "Барболина Екатерина Сергеевна", 101, 2, "+7 (999) 999-99-99", 10)
teacher1 = Teacher("Барболина", "Екатерина", "Сергеевна", department, 1980, 2005, 15, "старший преподаватель", "женский", "ул. Пушкина, д. 10, кв. 5", "Москва", "+7 (999) 888-88-88")
discipline1 = Discipline("Математический анализ", department, teacher1, 120, "экзамен")

student1 = Student("Барболина", "Екатерина", "Сергеевна", department, 2000, "женский", "ул. Ленина, д. 23, кв. 12", "Москва", "+7 (999) 777-77-77")
performance1 = AcademicPerformance(teacher1, discipline1, student1, 5)

department.add_discipline(discipline1)
teacher1.add_discipline(discipline1)
student1.add_academic_performance(performance1)
discipline1.add_academic_performance(performance1)

print("Имя студента:", student1.last_name, student1.first_name, student1.patronymic)
