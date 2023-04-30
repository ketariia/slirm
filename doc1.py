class Discipline:
    """
    Initializes a new instance of the Discipline class.

    Args:
        name (str): The name of the discipline.
        teacher (Teacher): The teacher who teaches the discipline.
    """
    def __init__(self, name: str, teacher: Teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.academic_performances = []

    def add_academic_performance(self, academic_performance: AcademicPerformance) -> None:
        """
        Adds an instance of the AcademicPerformance class to the list of academic performances for this discipline.

        Args:
            academic_performance (AcademicPerformance): The academic performance to be added.
        """
        self.academic_performances.append(academic_performance)


class Department:
    """
    Initializes a new instance of the Department class.

    Args:
        name (str): The name of the department.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.disciplines = []

    def add_discipline(self, discipline: Discipline) -> None:
        """
        Adds an instance of the Discipline class to the list of disciplines for this department.

        Args:
            discipline (Discipline): The discipline to be added.
        """
        self.disciplines.append(discipline)

class Teacher:
    """
    Initializes a new instance of the Teacher class.

    Args:
        name (str): The name of the teacher.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.disciplines = []

    def add_discipline(self, discipline: Discipline) -> None:
        """
        Adds an instance of the Discipline class to the list of disciplines this teacher teaches.

        Args:
            discipline (Discipline): The discipline to be added.
        """
        self.disciplines.append(discipline)
class AcademicPerformance:
    """
    Initializes a new instance of the AcademicPerformance class.

    Args:
        discipline (Discipline): The discipline for which this academic performance is for.
        student (Student): The student to whom this academic performance belongs.
        grade (float): The grade for this academic performance.
    """
    def __init__(self, discipline: Discipline, student: Student, grade: float) -> None:
        self.discipline = discipline
        self.student = student
        self.grade = grade
