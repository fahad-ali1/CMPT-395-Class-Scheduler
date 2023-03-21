"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: Rough idea of a course structure
"""
import csv
import re

import openpyxl
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
    def __init__(self, classroom, cohortName="", size=0):
        self.cohortName = cohortName
        self.classroom = classroom
        self.size = size
        self.mainProgramCourses = []  # program class
        self.electiveProgramCourses = []  # program class

    def __repr__(self):
        return f"{self.cohortName} - {self.classroom.classRoomNumber}, {self.size}/{self.classroom.normalCapacity}"


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
        self.currentStudents = normalCapacity
        self.lab = lab
        self.inUse = False
        self.isGhost = False
        self.schedule = None

    def setGhost(self):
        self.isGhost = True

    def setSchedule(self, schedule):
        self.schedule = schedule

    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity, \
              "lab: ", self.lab, " isGhost: ", self.isGhost)


class ScheduleNode:
    def __init__(self, time, cohort, start_date, end_date):
        self.time = time
        self.cohort = cohort
        self.start_date = start_date
        self.end_date = end_date
        self.prev = None
        self.next = None


def getClassrooms():
    wb = load_workbook('AllCourses.xlsx')
    allClassrooms = []
    ws = wb.worksheets[8]
    for i in range(2, ws.max_row + 1):
        if "Lab" in ws['A' + str(i)].value:
            classroom = Classroom(ws['A' + str(i)].value, ws['B' + str(i)].value, True)
            allClassrooms.append(classroom)
        else:
            classroom = Classroom(ws['A' + str(i)].value, ws['B' + str(i)].value)
            allClassrooms.append(classroom)
    return allClassrooms


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

'''
Returns a list of lists. Inner list is the number of students per term for each program.
List order is as follows:
BCOM
PCOM
PM
BA
SCMT
BK
FS
DXD
Example: [[1,2,3],[4,5,6],[7,8,9]]
index 0: BCOM term 1,2,3
index 1: PCOM term 1,2,3
index 3: PM term 1,2,3
'''
def getProgramNumbers(fileName):
    try:
        wb = load_workbook(fileName)
        # wb = load_workbook("semester_data.xlsx") #fast testing
        ws = wb.active
        programNumbersList = []
        for i in range(2, ws.max_row + 1):
            programNumbersList.append([ws['B' + str(i)].value, ws['C' + str(i)].value, ws['D' + str(i)].value])
        return programNumbersList
    except:
        # print("Error: File not found")
        return -1
