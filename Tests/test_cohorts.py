"""
Author: Schuyle Kelly
Purpose: Testing cohort object
"""

import unittest
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

    def test_iteration(self):
        self.students1.iterate_classrooms(100)

if __name__ == "__main__":
    unittest.main()
