from Course import *
from Cohort import *

courseName = "Courses_eg.csv"

courses_01 = readSaveCourse(courseName)

"""
Need to add a pre-req validator, creating classes from file and 
    (searching mechanism).

New: Excel implementation, "ability to provide the number of students via a file
or manually, so i con have more flexibility

"""

if __name__ == "__main__":

    print("\nCohort and Course Sprint 1 Demo\n")

    displaySavedCourses(courses_01)

