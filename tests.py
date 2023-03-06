"""
Author: Schuyler Kelly
Purpose:
    Testing the functions in the student module.
"""

from Students.students import *
import unittest

class TestStudents(unittest.TestCase):

    def setUp(self):
        # Set up a few different student objects with different input values
        # for number of students
        self.students1 = Students()
        self.students2 = Students()

        self.students1._PCOMStudents = 210
        self.students1._BCOMStudents = 25
        self.students1._BAStudents = 74
        self.students1._PMStudents = 102
        self.students1._SCMTStudents = 41
        self.students1._FSStudents = 18
        self.students1._DXDStudents = 0
        self.students1._BKStudents = 0
        self.students1._term = 1

        # Open classroom data and read it into a list
        self.rooms = []
        with open ("data/classrooms.csv", "r") as data:
            self.rooms = [l.strip() for l in data if "sep=" not in l]
        print(self.rooms)


    def test_GivenCohort_whenCohortIsFirst_ThenDividesEquallyIntoClass(self):
        self.assertEqual(self.students1.most_even_rooms(), [10, 10, 10])


if __name__ == "__main__":
    unittest.main()

