from .storage import load_data, save_data
from .models import Student, Course, Enrollment


def add_student(name) -> int:
    data = load_data()
    students = data["students"]

    new_id = 1 if not students else max(s["id"] for s in students) + 1
    students.append({
        "id": new_id,
        "name": name.strip()
    })
    save_data(data)
    return new_id


def add_course(code, title):
    data = load_data()
    data["courses"].append({"code": code, "title": title})
    save_data(data)


def enroll(student_id, course_code):
    data = load_data()
    data["enrollments"].append({
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    })
    save_data(data)


def add_grade(student_id, course_code, grade):
    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            if not (0 <= grade <= 100):
                raise ValueError("Invalid grade")
            e["grades"].append(grade)
            save_data(data)
            return

    raise ValueError("Enrollment not found")


def compute_average(student_id, course_code):
    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            if not e["grades"]:
                return 0
            return sum(e["grades"]) / len(e["grades"])

    raise ValueError("Enrollment not found")


def compute_gpa(student_id):
    data = load_data()

    averages = [
        sum(e["grades"]) / len(e["grades"])
        for e in data["enrollments"]
        if e["student_id"] == student_id and e["grades"]
    ]

    return sum(averages) / len(averages) if averages else 0
