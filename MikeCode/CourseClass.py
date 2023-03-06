"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: Rough idea of a course structure
"""
import csv
import re

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


class Program:
    def __init__(self, programType=""):
        self.programType = programType
        self.term1 = []
        self.term2 = []
        self.term3 = []

    def addToTerm(self, course, termNum):
        if termNum == 1:
            self.term1.append(course)
        elif termNum == 2:
            self.term2.append(course)
        elif termNum == 3:
            self.term3.append(course)

    def addProgramType(self, programType):
        self.programType = programType

    def printProgram(self):
        print(self.programType)

    def getAllTerms(self):
        allTerms = []
        allTerms.append(self.term1)
        allTerms.append(self.term2)
        allTerms.append(self.term3)
        return allTerms


class Cohort:
    def __init__(self, cohortName="", size=0):
        self.cohortName = cohortName
        self.size = size
        self.course = []


class Schedule:
    def __init__(self, day="", courseName="", timeSlot="", cohortName=""):
        self.day = day
        self.courseName = courseName
        self.timeSlot = timeSlot
        self.cohortName = cohortName
        self.currentCapacity = 0


class Classroom:
    def __init__(self, classRoomNumber='', normalCapacity=0, lab=False):
        self.classRoomNumber = classRoomNumber
        self.normalCapacity = normalCapacity
        self.lab = lab
        self.isGhost = False
        self.schedule = []

    def setGhost(self):
        self.isGhost = True

    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity, \
              "lab: ", self.lab, " isGhost: ", self.isGhost)


def getClassrooms(fileName):
    classroomList = []
    try:
        with open(fileName) as fileObject:
            # discard header
            next(fileObject)
            reader_obj = csv.reader(fileObject)
            # for loop to create a classroom object out of each row
            # after classroom is created, add classroom to a classroom list
            for row in reader_obj:
                # set lab flag to true for lab
                if "Lab" in row[0]:
                    classroom = Classroom(row[0], row[1], True)
                    classroomList.append(classroom)
                else:
                    classroom = Classroom(row[0], row[1])
                    classroomList.append(classroom)
    except:
        print('Error: file not found')
    return classroomList


def getProgramCourses(fileName):
    program = Program()
    counter = 0
    try:
        with open(fileName) as fileObject:
            programName = next(fileObject)
            program.addProgramType(programName)
            reader_obj = csv.reader(fileObject)
            for row in reader_obj:
                if re.search('Term [1-3]', row[0]):
                    counter += 1
                    pass
                else:
                    formattedDescript = re.sub('~>', ',', row[1])
                    course = Course(row[0], formattedDescript, row[2])
                    program.addToTerm(course, counter)
    except:
        print('Error: file not found')
    return program
