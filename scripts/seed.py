from gradebook import service

# Add Students
s1 = service.add_student("Alice")
s2 = service.add_student("Bob")
s3 = service.add_student("Charlie")
s4 = service.add_student("Filan")

# Add Courses
service.add_course("CS101", "Intro to CS")
service.add_course("MATH101", "Calculus I")
service.add_course("ENG101", "English Lit")

# Enroll Students
service.enroll(s1, "CS101")
service.enroll(s1, "MATH101")

service.enroll(s2, "CS101")
service.enroll(s2, "ENG101")

service.enroll(s3, "CS101")
service.enroll(s3, "MATH101")
service.enroll(s3, "ENG101")

service.enroll(s4, "ENG101")
service.enroll(s4, "CS101")

# Add Grades
service.add_grade(s1, "CS101", 90)
service.add_grade(s1, "MATH101", 85)

service.add_grade(s2, "CS101", 80)
service.add_grade(s2, "ENG101", 88)

service.add_grade(s3, "CS101", 75)
service.add_grade(s3, "MATH101", 95)
service.add_grade(s3, "ENG101", 82)

service.add_grade(s4, "ENG101", 95)
service.add_grade(s4, "CS101", 88)

print("Seed data added successfully!")
