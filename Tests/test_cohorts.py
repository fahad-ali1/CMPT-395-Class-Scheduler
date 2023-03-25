"""
Author: Schuyle Kelly
Purpose: Testing cohort object
"""

import unittest, sys
from lib.cohorts import Students
from lib.classrooms import Classroom


class TestStudents(unittest.TestCase):

    def setUp(self):
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
        
    def test_givenTooManyStudentsForRoomCombo_ThenReturnsZero(self):
    
        classlist1 = (
            Classroom("11-533", 36),
        )
        
        classlist2 = (
            Classroom("11-533", 36),
            Classroom("11-534", 36),
        )
        
        classlist3 = (
            Classroom("11-533", 36),
            Classroom("11-534", 36),
            Classroom("11-560", 24),
        )
        
        classlist4 = (
            Classroom("11-533", 36),
            Classroom("11-534", 36),
            Classroom("11-560", 24),
            Classroom("11-562", 24),
        )
        
        self.assertEqual(self.students1._check_space(classlist1, 40), -4)
        self.assertEqual(self.students1._check_space(classlist1, 36), 0)
        self.assertEqual(self.students1._check_space(classlist1, 32), 4)
        
        self.assertEqual(self.students1._check_space(classlist2, 76), -4)
        self.assertEqual(self.students1._check_space(classlist2, 72), 0)
        self.assertEqual(self.students1._check_space(classlist2, 68), 4)
        
        self.assertEqual(self.students1._check_space(classlist3, 101), -5)
        self.assertEqual(self.students1._check_space(classlist3, 96), 0)
        self.assertEqual(self.students1._check_space(classlist3, 91), 5)
        
        self.assertEqual(self.students1._check_space(classlist4, 125), -5)
        self.assertEqual(self.students1._check_space(classlist4, 120), 0)
        self.assertEqual(self.students1._check_space(classlist4, 115), 5)

    def test_givenConditionalWhileLoopExitCondition_ThenShouldAlwaysEventuallyExit(self):
        
        # Creates a log file because this is difficult if not impossible to measure
        # without inspection
        standard_stdout = sys.stdout
        with open('Tests/logs/cohort_iterator_test.log', 'w') as file:
            sys.stdout = file
            print(f"Students._iterate_classrooms(10) = {self.students1._iterate_classrooms(10)}")
            print(f"Students._iterate_classrooms(20) = {self.students1._iterate_classrooms(20)}")
            print(f"Students._iterate_classrooms(30) = {self.students1._iterate_classrooms(30)}")
            print(f"Students._iterate_classrooms(39) = {self.students1._iterate_classrooms(39)}")
            print(f"Students._iterate_classrooms(40) = {self.students1._iterate_classrooms(40)}")
            print(f"Students._iterate_classrooms(50) = {self.students1._iterate_classrooms(50)}")
            print(f"Students._iterate_classrooms(60) = {self.students1._iterate_classrooms(60)}")
            print(f"Students._iterate_classrooms(70) = {self.students1._iterate_classrooms(70)}")
            print(f"Students._iterate_classrooms(80) = {self.students1._iterate_classrooms(80)}")
            print(f"Students._iterate_classrooms(90) = {self.students1._iterate_classrooms(90)}")
            print(f"Students._iterate_classrooms(100) = {self.students1._iterate_classrooms(100)}")
            print(f"Students._iterate_classrooms(200) = {self.students1._iterate_classrooms(200)}")
            print(f"Students._iterate_classrooms(300) = {self.students1._iterate_classrooms(300)}")
            print(f"Students._iterate_classrooms(400) = {self.students1._iterate_classrooms(400)}")
            print(f"Students._iterate_classrooms(500) = {self.students1._iterate_classrooms(500)}")
            print(f"Students._iterate_classrooms(600) = {self.students1._iterate_classrooms(600)}")
            print(f"Students._iterate_classrooms(700) = {self.students1._iterate_classrooms(700)}")
            print(f"Students._iterate_classrooms(800) = {self.students1._iterate_classrooms(800)}")
            print(f"Students._iterate_classrooms(1000) = {self.students1._iterate_classrooms(1000)}")
            sys.stdout = standard_stdout
            
    def test_givenStudentCount_thenCohortsAreCreatedCorrectly(self):
        
        standard_stdout = sys.stdout
        with open("Tests/logs/create_cohorts_test.log", "w") as file:
            sys.stdout = file
            print(self.students1.divide_to_cohorts(40, "PC"))
            print(self.students1.divide_to_cohorts(50, "BC"))
            print(self.students1.divide_to_cohorts(80, "PM"))
            print(self.students1.divide_to_cohorts(400, "DXD"))
            print(self.students1.divide_to_cohorts(30, "FS"))
            self.students1._reset_classrooms(self.students1._rooms)
            print("======== CLASSROOMS RESET =========")
            print(self.students1.divide_to_cohorts(200, "PC"))
            print(self.students1.divide_to_cohorts(400, "BC"))
            print(self.students1.divide_to_cohorts(80, "PM"))
            sys.stdout = standard_stdout


if __name__ == "__main__":
    unittest.main()
