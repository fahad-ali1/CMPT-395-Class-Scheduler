"""
Author: Mike Lee
Purpose: Handle file input/output
"""

import csv, re, openpyxl
from openpyxl.reader.excel import load_workbook


"""
Purpose: Reads classroom info from an excel file
Parameters: None
Returns: list of classrooms
"""
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


"""
Purpose: Reads program info from an excel file
Parameters: None
Returns: List of programs
"""
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

