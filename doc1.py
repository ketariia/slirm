class AcademicPerformance:
    """
    Initializes a new instance of the AcademicPerformance class.

    Args:
        discipline (Discipline): The discipline for which this academic performance is for.
        student (Student): The student to whom this academic performance belongs.
        grade (float): The grade for this academic performance.
    """
    def __init__(self, discipline: "Discipline", student: "Student", grade: float) -> None:
        self.discipline = discipline
        self.student = student
        self.grade = grade

    def __str__(self) -> str:
        """
        Returns a string representation of the AcademicPerformance object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.student.name} received a {self.grade} in {self.discipline.name}"

    def __add__(self, other: "AcademicPerformance") -> "AcademicPerformance":
        """
        Adds two AcademicPerformance objects together.

        Args:
            other (AcademicPerformance): The AcademicPerformance object to add.

        Returns:
            AcademicPerformance: An instance of AcademicPerformance with the sum of the grades.
        """
        new_grade = self.grade + other.grade
        return AcademicPerformance(self.discipline, self.student, new_grade)

    def __sub__(self, other: "AcademicPerformance") -> "AcademicPerformance":
        """
        Subtracts one AcademicPerformance object from another.

        Args:
            other (AcademicPerformance): The AcademicPerformance object to subtract.

        Returns:
            AcademicPerformance: An instance of AcademicPerformance with the difference of the grades.
        """
        new_grade = self.grade - other.grade
        return AcademicPerformance(self.discipline, self.student, new_grade)

    def __mul__(self, other: float) -> "AcademicPerformance":
        """
        Multiplies an AcademicPerformance object by a float.

        Args:
            other (float): The float to multiply by.

        Returns:
            AcademicPerformance: An instance of AcademicPerformance with the multiplied grade.
        """
        new_grade = self.grade * other
        return AcademicPerformance(self.discipline, self.student, new_grade)

    def __truediv__(self, other: float) -> "AcademicPerformance":
        """
        Divides an AcademicPerformance object by a float.

        Args:
            other (float): The float to divide by.

        Returns:
            AcademicPerformance: An instance of AcademicPerformance with the divided grade.
        """
        new_grade = self.grade / other
        return AcademicPerformance(self.discipline, self.student, new_grade)
ap1 = AcademicPerformance(discipline1, student1, 4.0)
ap2 = AcademicPerformance(discipline1, student1, 3.5)

# Add two AcademicPerformance objects
ap3 = ap1 + ap2
print(ap3.grade)  # Output: 7.5

# Subtract one AcademicPerformance object from another
ap4 = ap1 - ap2
print(ap4.grade)  # Output: 0.5

# Multiply an AcademicPerformance object by a float
ap5 = ap1 * 2
print(ap5.grade)  # Output: 8.0

# Divide an AcademicPerformance object by a float
ap6 = ap1 / 2
print(ap6.grade)  # Output: 2.0
