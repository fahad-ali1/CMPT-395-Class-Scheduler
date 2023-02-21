"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: Rough idea of a course structure
"""
import csv
import re

from openpyxl.reader.excel import load_workbook


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


# Cohort Class takes in a cohort name and size initially
# Methods will be created to add a programs to mainProgramCourses
# and electiveProgramCourses


class Cohort:
    def __init__(self, cohortName="", size=0):
        self.cohortName = cohortName
        self.size = size
        self.mainProgramCourses = []  # program class
        self.electiveProgramCourses = []  # program class


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

'''
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
    '''


def getAllPrograms():
    wb = load_workbook('AllCourses.xlsx')
    term = None
    allPrograms = []
    for i in range(0, 8):
        ws1 = wb.worksheets[i]
        program = Program(programType=ws1.title)
        for j in range(2, ws1.max_row + 1):
            if re.search('Term [1-3]', ws1['A' + str(j)].value):
                term = ws1['A' + str(j)].value
            elif ws1['B' + str(j)].value is not None:
                course = Course(courseName=ws1['A' + str(j)].value, courseDescript=ws1['B' + str(j)].value, \
                                totalTranscriptHours=ws1['C' + str(j)].value)
                program.addToTerm(course, term)
        allPrograms.append(program)
    return allPrograms


getAllPrograms()