import unittest
from gradebook import service


class TestService(unittest.TestCase):

    def test_add_student(self):
        sid = service.add_student("Test Student")
        self.assertTrue(sid > 0)

    def test_add_grade_invalid(self):
        with self.assertRaises(ValueError):
            service.add_grade(999, "CS101", 90)

    def test_compute_average(self):
        sid = service.add_student("Avg Student")
        service.add_course("CS50", "Intro")
        service.enroll(sid, "CS50")
        service.add_grade(sid, "CS50", 100)
        self.assertEqual(service.compute_average(sid, "CS50"), 100)


if __name__ == "__main__":
    unittest.main()
