"""
Author: Mike Lee
Date: 01/02/2023
Purpose: Rough idea of a course structure
"""


class Course:
    def __init__(self, courseName="", courseDescript="", totalTranscriptHours=0, lectureLength=0, isLab=False):
        self.courseName = courseName
        self.courseDescript = courseDescript
        self.totalTranscriptHours = totalTranscriptHours
        self.lectureLength = lectureLength
        self.isLab = isLab
        self.startDate = "functionality coming soon"
        self.endDate = "functionality coming soon"

    def printCourseDetails(self):
        print(self.courseName, " ", self.courseDescript, " ", self.totalTranscriptHours)

    def getEndDate(self):
        # functionality coming soon
        pass

    def getStartDate(self):
        # functionality coming soon
        pass

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setCourseDes(self, courseDes):
        self.courseDescript = courseDes

    def setTranscriptHours(self, transcriptHours):
        self.totalTranscriptHours = transcriptHours


class Program:
    def __init__(self, programType=""):
        self.programType = programType
        self.term1 = []
        self.term2 = []
        self.term3 = []

    def setProgram(self, programName):
        self.programType = programName

    def addToTerm(self, course, termNum):
        if termNum == "Term 1":
            self.term1.append(course)
        elif termNum == "Term 2":
            self.term2.append(course)
        elif termNum == "Term 3":
            self.term3.append(course)

    def addProgramType(self, programType):
        self.programType = programType

    def printProgram(self):
        print(self.programType)

    def getAllTerms(self):
        allTerms = [self.term1, self.term2, self.term3]
        return allTerms


class Schedule:
    def __init__(self, day="", courseName="", timeSlot="", cohortName=""):
        self.day = day
        self.courseName = courseName
        self.timeSlot = timeSlot
        self.cohortName = cohortName
        self.currentCapacity = 0


class ScheduleNode:
    def __init__(self, time, cohort, start_date, end_date):
        self.time = time
        self.cohort = cohort
        self.start_date = start_date
        self.end_date = end_date
        self.prev = None
        self.next = None


