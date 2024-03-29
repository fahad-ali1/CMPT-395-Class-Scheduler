"""
Author: Schuyler Kelly, Mike Lee
Purpose: Testing scheduler
"""

import unittest, sys, random
from lib.fileio import getAllPrograms
from lib.cohorts import Students
from lib.classrooms import Classroom
from lib.scheduler import Week, Day, Scheduler


class TestScheduler(unittest.TestCase):

    def setUp(self):
    
        self.week1 = Week(0)
        self.week2 = Week(0)
        self.week3 = Week(0)
        self.scheduler = Scheduler()
        
        #cohort_nums = [random.randint(30, 200) for _ in range(8)]
        self.students1 = Students()
        self.students1._PCOMStudents = 40
        self.students1._BCOMStudents = 40
        self.students1._term = 1
        self.cohort_list = self.students1.cohorts_final()
        self.PCOM_cohorts = self.cohort_list[0]
        self.BCOM_cohorts = self.cohort_list[1]
        self.PCOM_and_BCOM_cohorts = self.PCOM_cohorts + self.BCOM_cohorts
        
    def test_givenScheduleCoursesFunction_whenRan_ShouldCreateSchedule(self):
        
        standard_stdout = sys.stdout

        with open("Tests/logs/scheduleCourses_test1.log", "w") as file:
            sys.stdout = file
            print(self.scheduler.scheduleCourses(self.week1, self.PCOM_cohorts))
            sys.stdout = standard_stdout

        with open("Tests/logs/scheduleCourses_test2.log", "w") as file:
            sys.stdout = file
            print(self.scheduler.scheduleCourses(self.week2, self.BCOM_cohorts))
            sys.stdout = standard_stdout

        with open("Tests/logs/scheduleCourses_test3.log", "w") as file:
            sys.stdout = file
            print(self.scheduler.scheduleCourses(self.week3, self.PCOM_and_BCOM_cohorts))
            sys.stdout = standard_stdout

    def test_givenSchdulerInitialized_then_ShouldCreateProperTimeMap(self):
        scheduler = Scheduler()


if __name__ == "__main__":
    unittest.main()
