from disp import AcademicPerformance, Department, Discipline, Student, Teacher


class University:
    def __init__(self):
        self.departments = []
        self.teachers = []
        self.disciplines = []
        self.students = []
        self.academic_performances = []

    def add_department(self, department):
        self.departments.append(department)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def add_student(self, student):
        self.students.append(student)

    def add_academic_performance(self, performance):
        self.academic_performances.append(performance)

# create a university
university = University()

# create a department
department1 = Department("Кафедра математики", "Факультет естественных наук", "Александрович Иван Алексеев", 101, 2, "+7 (999) 999-99-99", 10)

# create a teacher
teacher1 = Teacher("Барболина", "Екатерина", "Сергеевна", department1, 1980, 2005, 15, "старший преподаватель", "женский", "ул. Пушкина, д. 10, кв. 5", "Москва", "+7 (999) 888-88-88")

# create a discipline
discipline1 = Discipline("Математический анализ", department1, teacher1, 120, "экзамен")

# create a student
student1 = Student("Александрович", "Иван", "Алексеев", department1, 2000, "мужской", "ул. Ленина, д. 23, кв. 12", "Москва", "+7 (999) 777-77-77")

# create an academic performance
performance1 = AcademicPerformance(teacher1, discipline1, student1, 5)

# add the department, teacher, discipline, student, and academic performance to the university
university.add_department(department1)
university.add_teacher(teacher1)
university.add_discipline(discipline1)
university.add_student(student1)
university.add_academic_performance(performance1)

# print the student's information
print(student1)

# print the student's grade in the academic performance
for performance in student1.academic_performances:
    print(performance.grade)
