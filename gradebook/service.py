from .storage import load_data, save_data
from .models import Student, Course, Enrollment


def add_student(name) -> int:
    """
    Add a new student to the gradebook.

    Args:
        name (str): Full name of the student.

    Returns:
        int: The ID assigned to the new student.
    """
    data = load_data()
    students = [Student(**s) for s in data["students"]]

    new_id = 1 if not students else max(s.id for s in students) + 1
    student = Student(new_id, name)
    students.append(student)

    # Save as dicts
    data["students"] = [vars(s) for s in students]
    save_data(data)
    return new_id


def add_course(code, title):
    """
    Add a new course to the gradebook.

    Args:
        code (str): Course code.
        title (str): Course title.

    Raises:
        ValueError: If course already exists.
    """
    data = load_data()
    courses = [Course(**c) for c in data["courses"]]

    code, title = code.strip(), title.strip()
    if any(c.code == code for c in courses):
        raise ValueError("Course already exists")

    course = Course(code, title)
    courses.append(course)

    data["courses"] = [vars(c) for c in courses]
    save_data(data)


def enroll(student_id, course_code):
    """
    Enroll a student in a course.

    Raises:
        ValueError: If student, course, or enrollment does not exist/already enrolled.
    """
    data = load_data()
    students = [Student(**s) for s in data["students"]]
    courses = [Course(**c) for c in data["courses"]]
    enrollments = [Enrollment(**e) for e in data["enrollments"]]

    if not any(s.id == student_id for s in students):
        raise ValueError("Student not found")
    if not any(c.code == course_code for c in courses):
        raise ValueError("Course not found")
    if any(e.student_id == student_id and e.course_code == course_code for e in enrollments):
        raise ValueError("Already enrolled")

    enrollment = Enrollment(student_id, course_code)
    enrollments.append(enrollment)

    data["enrollments"] = [vars(e) for e in enrollments]
    save_data(data)


def add_grade(student_id, course_code, grade):
    """
    Add a grade for a student in a specific course.

    Raises:
        ValueError: If student, course, enrollment does not exist, or grade invalid.
    """
    data = load_data()
    students = [Student(**s) for s in data["students"]]
    courses = [Course(**c) for c in data["courses"]]
    enrollments = [Enrollment(**e) for e in data["enrollments"]]

    if not any(s.id == student_id for s in students):
        raise ValueError("Student not found")
    if not any(c.code == course_code for c in courses):
        raise ValueError("Course not found")

    for e in enrollments:
        if e.student_id == student_id and e.course_code == course_code:
            e._validate_grade(grade)
            e.grades.append(grade)
            data["enrollments"] = [vars(en) for en in enrollments]
            save_data(data)
            return

    raise ValueError("Enrollment not found")


def compute_average(student_id, course_code) -> float:
    """
    Compute the average grade for a student in a specific course.

    Returns:
        float: Average grade (0 if no grades exist).
    """
    data = load_data()
    enrollments = [Enrollment(**e) for e in data["enrollments"]]

    for e in enrollments:
        if e.student_id == student_id and e.course_code == course_code:
            return sum(e.grades) / len(e.grades) if e.grades else 0

    raise ValueError("Enrollment not found")


def compute_gpa(student_id) -> float:
    """
    Compute GPA for a student across all courses.

    Returns:
        float: Average of course averages (0 if no grades exist).
    """
    data = load_data()
    enrollments = [Enrollment(**e) for e in data["enrollments"]
                   if e["student_id"] == student_id]

    averages = [sum(e.grades)/len(e.grades) for e in enrollments if e.grades]
    return sum(averages)/len(averages) if averages else 0
