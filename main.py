import argparse
from gradebook import service


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    # Add student
    s = sub.add_parser("add-student")
    s.add_argument("--name", required=True)

    # Add course
    c = sub.add_parser("add-course")
    c.add_argument("--code", required=True)
    c.add_argument("--title", required=True)

    # Enroll student
    e = sub.add_parser("enroll")
    e.add_argument("--student-id", type=int, required=True)
    e.add_argument("--course", required=True)

    # Add grade
    g = sub.add_parser("add-grade")
    g.add_argument("--student-id", type=int, required=True)
    g.add_argument("--course", required=True)
    g.add_argument("--grade", type=int, required=True)

    # Compute average
    avg = sub.add_parser("avg")
    avg.add_argument("--student-id", type=int, required=True)
    avg.add_argument("--course", required=True)

    # Compute GPA
    gpa = sub.add_parser("gpa")
    gpa.add_argument("--student-id", type=int, required=True)

    # List data
    lst = sub.add_parser("list")
    lst.add_argument("type", choices=["students", "courses", "enrollments"])

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            sid = service.add_student(args.name)
            print(f"Added student {args.name} with ID {sid}")

        elif args.command == "add-course":
            service.add_course(args.code, args.title)
            print(f"Added course {args.code} - {args.title}")

        elif args.command == "enroll":
            service.enroll(args.student_id, args.course)
            print(
                f"Student {args.student_id} enrolled in course {args.course}")

        elif args.command == "add-grade":
            service.add_grade(args.student_id, args.course, args.grade)
            print(
                f"Added grade {args.grade} for student {args.student_id} in course {args.course}")

        elif args.command == "avg":
            avg_score = service.compute_average(args.student_id, args.course)
            print(
                f"Average grade for student {args.student_id} in {args.course}: {avg_score}")

        elif args.command == "gpa":
            gpa_score = service.compute_gpa(args.student_id)
            print(f"GPA for student {args.student_id}: {gpa_score}")

        elif args.command == "list":
            if args.type == "students":
                for s in service.load_data()["students"]:
                    print(f"{s['id']}: {s['name']}")
            elif args.type == "courses":
                for c in service.load_data()["courses"]:
                    print(f"{c['code']}: {c['title']}")
            elif args.type == "enrollments":
                for e in service.load_data()["enrollments"]:
                    print(
                        f"Student {e['student_id']} -> {e['course_code']}, Grades: {e['grades']}")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
