import argparse
from gradebook import service


def main():
    """
    Parse CLI arguments and execute the corresponding gradebook service functions.

    Handles:
        - add-student: Adds a new student.
        - add-grade: Adds a grade for an existing student in a course.

    Errors are caught and printed to the console.
    """
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    s = sub.add_parser("add-student")
    s.add_argument("--name")

    g = sub.add_parser("add-grade")
    g.add_argument("--student-id", type=int)
    g.add_argument("--course")
    g.add_argument("--grade", type=int)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            sid = service.add_student(args.name)
            print(f"Student added with ID {sid}")

        elif args.command == "add-grade":
            service.add_grade(args.student_id, args.course, args.grade)
            print("Grade added")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
