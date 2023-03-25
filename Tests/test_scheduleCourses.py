"""
Author: Schuyler Kelly, Mike Lee
Purpose: Testing scheduler
"""

import unittest, sys, random
from lib.fileio import getAllPrograms
from lib.cohorts import Students
from lib.classrooms import Classroom
from lib.scheduler import Week, Day
from Tests.schedtest import scheduleCourses


class TestScheduler(unittest.TestCase):

    def setUp(self):
    
        self.week = Week(0)
        #cohort_nums = [random.randint(30, 200) for _ in range(8)]
        self.students1 = Students()
        self.students1._PCOMStudents = 30
        self.students1._term = 1
        self.cohort_list = self.students1.cohorts_final()
        self.PCOM_cohorts = self.cohort_list[0]
        
    def test_givenScheduleCoursesFunction_whenRan_ShouldCreateSchedule(self):
        
        standard_stdout = sys.stdout
        with open("Tests/logs/scheduleCourses_test.log", "w") as file:
            sys.stdout = file
            print(scheduleCourses(self.week, self.PCOM_cohorts))
            sys.stdout = standard_stdout


if __name__ == "__main__":
    unittest.main()
