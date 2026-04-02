class Student:
    """
    Represents a student in the gradebook system.

    Attributes:
        id (int): A unique identifier for the student.
        name (str): The full name of the student.
    """

    def __init__(self, id: int, name: str):
        """
        Initializes a Student instance.

        Raises:
            ValueError: If the name is empty or only whitespace.
        """
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.id = id
        self.name = name.strip()

    def __str__(self):
        return f"Student: {self.name}, id: {self.id}"


class Course:
    """
    Represents an academic course.

    Attributes:
        code (str): The unique course code (e.g., 'CS101').
        title (str): The descriptive title of the course.
    """

    def __init__(self, code: str, title: str):
        """
        Initializes a Course instance.

        Raises:
            ValueError: If code or title are empty.
        """
        if not code.strip() or not title.strip():
            raise ValueError("Course code and title are required.")

        self.code = code.strip().upper()
        self.title = title.strip()

    def __str__(self):
        return f"Course code: {self.code}, Course title: {self.title}"


class Enrollment:
    """
    Links a student to a specific course and tracks their grades.

    Attributes:
        student_id (int): The ID of the enrolled student.
        course_code (str): The code of the course.
        grades (list[float]): A list of numeric grades (0-100).
    """

    def __init__(self, student_id: int, course_code: str, grades: list[int] = None):
        self.student_id = student_id
        self.course_code = course_code.strip().upper()
        self.grades = grades if grades is not None else []

        # Validation: Check existing grades if passed in
        for g in self.grades:
            self._validate_grade(g)

    def _validate_grade(self, grade):
        """Internal helper to check if a grade is valid."""
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError(
                f"Invalid grade: {grade}. Must be a number between 0 and 100.")

    def __str__(self):
        return f"Student id: {self.student_id}, Course code: {self.course_code}, Grades: {self.grades}"
