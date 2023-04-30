class Discipline:
    def __init__(self, name: str, teacher: "Teacher") -> None:
        self.name = name
        self.teacher = teacher


class Department:
    def __init__(self, name: str, disciplines: List["Discipline"]) -> None:
        self.name = name
        self.disciplines = disciplines


class Teacher:
    def __init__(self, name: str) -> None:
        self.name = name


class Student:
    def __init__(self, name: str, department: "Department") -> None:
        self.name = name
        self.department = department


class AcademicPerformance:
    def __init__(self, discipline: "Discipline", student: "Student", grade: float) -> None:
        self.discipline = discipline
        self.student = student
        self.grade = grade


import time
from functools import wraps
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        end = time.monotonic()
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper


def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} times.")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"Function {func.__name__} was called with args {args} and kwargs {kwargs}\\n")
        return func(*args, **kwargs)
    return wrapper


class Discipline:
    def __init__(self, name: str, teacher: "Teacher") -> None:
        self.name = name
        self.teacher = teacher

    @logger
    def __str__(self) -> str:
        return f"{self.name} (taught by {self.teacher.name})"


class Department:
    def __init__(self, name: str, disciplines: List["Discipline"]) -> None:
        self.name = name
        self.disciplines = disciplines

    @logger
    def __str__(self) -> str:
        discipline_names = [d.name for d in self.disciplines]
        return f"{self.name} ({', '.join(discipline_names)})"


class Teacher:
    def __init__(self, name: str) -> None:
        self.name = name

    @logger
    def __str__(self) -> str:
        return self.name


class Student:
    def __init__(self, name: str, department: "Department") -> None:
        self.name = name
        self.department = department

    @logger
    def __str__(self) -> str:
        return f"{self.name} ({self.department.name})"


class AcademicPerformance:
    def __init__(self, discipline: "Discipline", student: "Student", grade: float) -> None:
        self.discipline = discipline
        self.student = student
        self.grade = grade

    @logger
    @time_it
    def __str__(self) -> str:
        return f"{self.student.name} received a {self.grade} in {self.discipline.name}"

    @logger
    @call_counter
    def get_grade(self) -> float:
        return self.grade