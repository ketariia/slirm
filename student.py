class Student:
    def __init__(self, surname, firstname, direction, group, marks):
        self.surname = surname
        self.firstname = firstname
        self.direction = direction
        self.group = group
        self.shares = 0
        self.marks = marks

    def calculate_average_mark(self):
        # Вычисляем средний балл на основе введённых оценок
        sum_of_marks = 0
        for mark in self.marks:
            sum_of_marks += mark
        return sum_of_marks / self.shares

    def print_data(self):
        print(f"{self.surname}, {self.firstname}")
        print("Направление: {self.direction}")
        print(f"Группа: {self.group}")
        print("Средний балл: {self.calculate_average_mark()}")
        
class StudentData:
    def __init__(self, students):
        self.students = students
        
    def print_data(self):
        for student in self.students:
            student.print_data()  #  add this line here
        
        
students = [
    Student('Иванов', 'Иван', 'Филологический', 'А', [3,5,3]),
    Student('Петров', 'Пётр', 'Физический', 'Б', [4,5,2,3]),
    Student('Смирнов', 'Сергей', 'Математический', 'В', [5,3,2]),
    Student('Рязанов', 'Юрий', 'Исторический', 'Г', [4,5,2]),
    Student('Алексеева', 'Ольга', 'Программирование', 'Д', [3,2,4]),
]
        
student_data = StudentData(students)
student_data.print_data()


