"""
Author: Sankalp Shrivastav
ID: 3106374
Date: 30/01/2023
Purpose: A basic idea for the course data structure

reference: 
    - https://www.geeksforgeeks.org/working-csv-files-python/
"""

import csv

class Course:

    def __init__(self, Name = "CMPT 101"):

        """
        Members for the Course class, contains name of the course, 
        any prequsites, duration of the course, time finished, and is the course
        completed.
        """
        
        self._name = Name
        self._discription = ""
        self._preReq = []
        self._classTime = 0
        self._timeDone = 0
        self._courseFinished = False

        # these features are examples, will need to be chaecked
    
    def setName(self, Name):

        #set the name of the course

        self._name = Name
    
    def isFinished(self) -> bool:

        """
        Check if the course is finished, 
        return : true is finished, false if not finished

        finished condition: if total required is equal to time done
                            Time Required = Time Done

        """

        if self._classTime <= self._timeDone:
            self._courseFinished = True; return True
        
        else: return False
    
    def canTakeCourse(self):
        """
        Will check if the student has met the prerequsite for the course
        """
        pass
    
    def courseInfo(self) -> str:
        """
        Display the string representation of the course
        """

        # self.isFinished()

        return  f"Course Name: {self._name}\n"\
                f"Course Prerequsites: {self._preReq}\n"\
                f"Course Time: {self._classTime}\n"\
                f"Course Time Done: {self._timeDone}\n"\
                f"Course Done:  {self._courseFinished}"
    
    def updateClassTime(self, Time):

        """
        Set Class Time (duration of the class) to Time
        """

        self._classTime = Time

    def addTimeDone(self, Time):

        """
        Add time to total time done for the class
        """

        self._timeDone += Time

    def addPreReq(self, preReq):

        """
        Adding a course to preReq
        """

        self._preReq.append(preReq)
    
    def addDescription(self, discription):

        """
        Add Description to the course object
        """

        self._discription = discription

def readSaveCourse(fileName):

    fields = []
    rows = []

    Courses = []

    with open(fileName, "r") as csvFile:

        csvreader = csv.reader(csvFile)
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)
 
    for row in rows[:]:

        course = Course(row[0])
        course.addDescription(row[1])
        course.updateClassTime(row[2])

        Courses.append(course)

        # print('\n')
    
    # for classes in Courses:

    #     print(f"\n{classes.courseInfo()}")
    
    # print("\n")

    return Courses

def displaySavedCourses(courses):

    for classes in courses:

        print(f"\n{classes.courseInfo()}")
    
    print("\n")


if __name__ == "__main__":

    print("Testing Course")

    # courses = ["abc101", "abc201"]

    # course1 = Course()
    # course2 = Course()

    # course1.setName(courses[0])
    # course2.setName(courses[1])
    # course1.updateClassTime(4)
    # course2.updateClassTime(2)
    # course1.addTimeDone(4.5)
    # course2.addTimeDone(1.5)
    # course2.addPreReq(courses[0])

    # print(f"\nCourses Information:\n\n{course1.courseInfo()}\n"\
    #         f"\n{course2.courseInfo()}\n\n")

    print("TESTING Read Write of Courses")

    fileName = "Courses_eg.csv"

    courses = readSaveCourse(fileName)

    displaySavedCourses(courses)
