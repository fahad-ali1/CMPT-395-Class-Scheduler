"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: Collection of classes and methods needed for the project
"""

import re

from openpyxl.reader.excel import load_workbook

# Course Class:
# Represents a course
# Attributes include:
# courseName = name of the course
# courseDescript = course description
# lectureLength = length of each lecture
# courseType = the type of each course(normal, online/virtual, lab)
class Course:
    def __init__(self, courseName="", courseDescript="", totalTranscriptHours=0):
        self.courseName = courseName
        self.courseDescript = courseDescript
        self.totalTranscriptHours = totalTranscriptHours
        self.lectureLength = 0.0
        self.courseType = ""

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setCourseDes(self, courseDes):
        self.courseDescript = courseDes

    def setTranscriptHours(self, transcriptHours):
        self.totalTranscriptHours = transcriptHours

    def setCourseType(self, status):
        self.courseType = status

    def setLectureLength(self, lecLen):
        self.lectureLength = lecLen

    def getcourseName(self):
        return self.courseName

    def getdescription(self):
        return self.courseDescript

    def getcourseType(self):
        return self.courseType

    def getLectureLength(self):
        return self.lectureLength

    def printCourseDetails(self):
        print(self.courseName, " ", self.courseDescript, " ", self.totalTranscriptHours)

# Program:
# Represents a program at macewan
# Attributes include:
# programType = the type(name) of the program
# term1 = list of all courses(course class) for term 1
# term2 = list of all courses(course class) for term 2
# term3 = list of all courses(course class) for term 3

class Program:
    def __init__(self, programType=""):
        self.programType = programType
        self.term1 = []
        self.term2 = []
        self.term3 = []

    def setProgram(self, programName):
        self.programType = programName

    def addToTerm(self, course, termNum):
        termNum = termNum.strip()
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

# Classroom:
# Represents a physical classroom
# Attributes include:
# classRoomNumber = classroom number/name
# normalCapacity = capacity
# lab = is it a lab
# isGhost = is it a ghost room (room that would be needed for extra students)
# schedule = schedule linked list representing the schedule
class Classroom:
    def __init__(self, classRoomNumber='', normalCapacity=0, lab=False):
        self.classRoomNumber = classRoomNumber
        self.normalCapacity = normalCapacity
        self.lab = lab
        self.isGhost = False
        self.schedule = None

    def setGhost(self):
        self.isGhost = True

    def setSchedule(self, schedule):
        self.schedule = schedule

    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity, \
              "lab: ", self.lab, " isGhost: ", self.isGhost)

# Cohort Class takes in a cohort name and size initially
# Methods will be created to add a programs to mainProgramCourses
# and electiveProgramCourses

class Cohort:
    def __init__(self, cohortName="", size=0):
        self.cohortName = cohortName
        self.size = size
        self.mainProgramCourses = []  # program class
        self.electiveProgramCourses = []  # program class

# ScheduleLinkedList:
# Represents a schedule for a classroom object
# Attributes include:
# totalHours = the total hours in a day that the classroom is available for
# head = head node of schedule (doubly linked list)
class ScheduleLinkedList:
    def __init__(self, totalHours=10):
        self.totalHours = totalHours
        self.head = None

    def addNodeEnd(self, time, cohort, start_date, end_date):
        timeBlock = ScheduleNode(time, cohort, start_date, end_date)
        if self.head is None:
            self.head = timeBlock
            return
        else:
            currentLink = self.head
            while currentLink.next:
                currentLink = currentLink.next
            timeBlock.prev = currentLink
            timeBlock.next = None

# ScheduleNode:
# Represents a lecture time block for a classroom's schedule
# Attributes include:
# time = lecture length
# cohort = cohort
# startDate = course scheduled start date
# endDate = course scheduled end date
# prev = prev lecture block (node)
# next = next lecture block (node)
class ScheduleNode:
    def __init__(self, time, cohort, start_date, end_date):
        self.time = time  # 1.5 8 - 950
        self.cohort = cohort
        self.startDate = start_date
        self.endDate = end_date
        self.prev = None
        self.next = None

# start/end is for schedule node

# getClassrooms:
# Helper Fucntion
# Purpose: Used to gather list of classroom objects representing all available classrooms
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

# getAllPrograms
# Helper Function
# Purpose: Used to gather a list of program objects representing all available programs at macewan
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
                pass

            elif ws1['B' + str(j)].value is not None:
                course = Course(courseName=ws1['A' + str(j)].value, courseDescript=ws1['B' + str(j)].value,
                                totalTranscriptHours=ws1['C' + str(j)].value)
                course.setCourseType(str(checkIfLab(ws1['E' + str(j)].value)))
                course.setLectureLength(float(getMinimumTime(ws1['F' + str(j)].value)))
                program.addToTerm(course, term)
        allPrograms.append(program)
    return allPrograms

# getProgramNumbers
# Helper Function
#
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
        print("Error: File not found")
        return -1

# Expected input: String or None type value from cell F of Allcourse.xlsx
# Expected output: If None type is found then return float indicating default lecture length is returned (1.5 hours)
# Else if value is found then return float indicating minimum lecture length
def getMinimumTime(data):
    if data is None:
        return 1.5
    else:
        return float(data[0])


# Expected input: value from cell E of AllCourse.xlsx
# Expected output: returns a string indicating the lab status of a course
def checkIfLab(data):
    if data is None:
        return "Normal"
    elif data == "Lab":
        return "Lab"
    elif data == "Both":
        return "Both"
    elif data == "Virtual":
        return "Virtual"
    elif data == "Online":
        return "Online"


'''
some notes:
1. make islab(method) - Course Class
2. method to check if prereq/isfinished - Course/cohort
3. make start/end date methods - course
4. **maybe- add course to master course file method
5. method for minimum timeslot(course) and number of sessiosn(default is 1.5)


salah code:
takes in a program name, cohort size, lecture/lab **24 hour format
what to return:
string of a course, string of a lecture/lab, timing(24 hr format)
example for 1.5 hour courses: 9-10.5
'''

'''
Legend for excel file codes:
SA = Schedule after all classes are done, end of the term
NBOA = Do not schedule immediately before or after other courses
Twice/Half = Class should be schedule twice a week half way through the term


'''