import unittest
from gradebook import service
from gradebook.storage import save_data


class TestService(unittest.TestCase):

    def setUp(self):
        """Reset data before each test."""
        empty_data = {
            "students": [],
            "courses": [],
            "enrollments": []
        }
        save_data(empty_data)

    def test_add_student(self):
        """Test that a student is added and receives a positive ID."""
        sid = service.add_student("Test Student")
        self.assertTrue(sid > 0)

    def test_add_grade_invalid(self):
        """Test adding a grade for a non-existent student or course raises ValueError."""
        with self.assertRaises(ValueError):
            service.add_grade(999, "CS101", 90)

    def test_add_grade_out_of_range(self):
        """Test adding a grade outside 0-100 range raises ValueError."""
        sid = service.add_student("OutRange")
        service.add_course("CS300", "Test Course")
        service.enroll(sid, "CS300")
        with self.assertRaises(ValueError):
            service.add_grade(sid, "CS300", 110)

    def test_compute_average(self):
        """Test computing the average for a single grade returns the correct value."""
        sid = service.add_student("Avg Student")
        service.add_course("CS50", "Intro")
        service.enroll(sid, "CS50")
        service.add_grade(sid, "CS50", 100)
        self.assertEqual(service.compute_average(sid, "CS50"), 100)

    def test_compute_average_multiple_grades(self):
        """Test computing the average for multiple grades returns the correct mean."""
        sid = service.add_student("MultiGrade")
        service.add_course("CS200", "Advanced CS")
        service.enroll(sid, "CS200")
        service.add_grade(sid, "CS200", 80)
        service.add_grade(sid, "CS200", 100)
        self.assertEqual(service.compute_average(sid, "CS200"), 90)

    def test_compute_gpa(self):
        """Test computing GPA across multiple courses returns the correct average."""
        sid = service.add_student("GPA Student")
        service.add_course("CS101", "Intro CS")
        service.add_course("MATH101", "Calculus")
        service.enroll(sid, "CS101")
        service.enroll(sid, "MATH101")
        service.add_grade(sid, "CS101", 90)
        service.add_grade(sid, "MATH101", 80)
        self.assertEqual(service.compute_gpa(sid), 85)

    def test_enroll_invalid_student(self):
        """Test enrolling a non-existent student raises ValueError."""
        with self.assertRaises(ValueError):
            service.enroll(999, "CS101")

    def test_enroll_invalid_course(self):
        """Test enrolling in a non-existent course raises ValueError."""
        sid = service.add_student("InvalidCourse")
        with self.assertRaises(ValueError):
            service.enroll(sid, "NONEXIST")


if __name__ == "__main__":
    unittest.main()
