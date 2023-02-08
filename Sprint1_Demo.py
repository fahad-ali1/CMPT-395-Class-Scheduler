from Course import *
from Cohort import *

courseName = "Courses_eg.csv"

courses_01 = readSaveCourse(courseName)


if __name__ == "__main__":

    print("\nCohort and Course Sprint 1 Demo\n")

    displaySavedCourses(courses_01)

