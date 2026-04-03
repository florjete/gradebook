# Gradebook CLI

A simple command-line application in Python for managing students, courses, enrollments, and grades.

---

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Commands](#commands)
- [Sample Data](#sample-data)
- [Design Decisions & Limitations](#design-decisions--limitations)
- [Tests](#tests)

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/florjete/gradebook-cli.git
cd gradebook-cli
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows (PowerShell)
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

---

## Usage

Run the CLI by executing `main.py` with the desired command:

```bash
python main.py <command> [options]
```

### Examples

```bash
# Add a student
python main.py add-student --name "John Doe"
# Output: Added student John Doe with ID 1

# Add a course
python main.py add-course --code CS101 --title "Intro to CS"
# Output: Added course CS101 - Intro to CS
python main.py add-course --code OS101 --title "Intro to Operating Systems"
# Output: Added course OS101 - Intro to Operating Systems


# Enroll a student
python main.py enroll --student-id 1 --course CS101
# Output: Student 1 enrolled in course CS101
python main.py enroll --student-id 1 --course OS101
# Output: Student 1 enrolled in course OS101

# Add a grade
python main.py add-grade --student-id 1 --course CS101 --grade 95
# Output: Added grade 95 for student 1 in course CS101
python main.py add-grade --student-id 1 --course CS101 --grade 65
# Output: Added grade 65 for student 1 in course CS101
python main.py add-grade --student-id 1 --course CS101 --grade 83
# Output: Added grade 83 for student 1 in course OS101

# Compute course average
python main.py avg --student-id 1 --course CS101
# Output: Average grade for student 1 in CS101: 80.0

# Compute GPA
python main.py gpa --student-id 1
# Output: GPA for student 1: 81.0

# List data
python main.py list students
python main.py list courses
python main.py list enrollments
```

---

## Commands

| Command       | Description                                     |
| ------------- | ----------------------------------------------- |
| `add-student` | Adds a new student                              |
| `add-course`  | Adds a new course                               |
| `enroll`      | Enrolls a student in a course                   |
| `add-grade`   | Adds a grade for a student in a course          |
| `avg`         | Computes the average grade for a student/course |
| `gpa`         | Computes GPA for a student                      |
| `list`        | Lists students, courses, or enrollments         |

---

## Sample Data

Populate the gradebook with sample students, courses, and enrollments:

```bash
python scripts/seed.py
```

---
## Sample Logs

Example of application logs:
<img width="1093" height="208" alt="image" src="https://github.com/user-attachments/assets/b941433b-2dd7-4d7a-acac-7109a82f24c5" />

---
## Design Decisions & Limitations

- JSON is used for storage instead of a database for simplicity.
- Service layer is stateless: loads and saves data on each operation.
- Basic validation is handled in models and service functions.
- CLI implemented using `argparse`.

**Limitations:**

- Not scalable (no database)
- Minimal input validation
- No authentication or GUI

---

## Tests

Run unit tests using:

```bash
python -m unittest discover tests
```
