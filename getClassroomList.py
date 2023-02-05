"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: takes in a .csv file and returns a list of classroom objects
"""

import csv
from Classroom import Classroom


def makeClassrooms(fileName):
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


#test
#makeClassrooms("Classrooms.csv")
