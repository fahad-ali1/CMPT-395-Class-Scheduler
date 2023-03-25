"""
Authors: Mike Lee, Schuyler Kelly
Purpose: Module centerd around creating cohorts, based on existing classrooms.
"""

import math, itertools

# Import local code
from lib.fileio import getClassrooms
from lib.classrooms import Classroom


"""
COHORT
------

ATTRIBUTES
----------
cohortName      - The name of the cohort (i.e. PC0101 or BC0203)
classroom       - The Classroom object assigned to the cohort
size            - Number of students in the cohort
programCourses  - A queue of courses the cohort must take
"""
class Cohort:
    def __init__(self, classroom, cohortName="", size=0):
        self.cohortName = cohortName
        self.classroom = classroom
        self.size = size
        self.programCourses = None  # program class
        self.currentCourses = None
        self.prereq = {}

    def __repr__(self):
        return f"{self.cohortName} - {self.classroom.classRoomNumber}, {self.size}/{self.classroom.normalCapacity}"

    def setmainProgram(self, program):
        self.programCourses = program

    def setClassroom(self, classroom):
        self.classroom = classroom

    def getCohortName(self):
        return self.cohortName

    def getMain(self):
        return self.mainProgramCourses 


"""
STUDENTS
--------

ATTRUBUTES
----------
All of the below attributes are the count of each student in each program. Assumes counts
in BCOM/PCOM are unique from electives.
****
_BCOMStudents, _PCOMStudents, _PMStudents
_BAStudents, _SCMTStudents, _FSStudents,
_DXDStudents, _BKStudents
****

_term   - The term the current students are in
_rooms  - The list of rooms the students can be placed into

METHODS
-------
cohorts_final() -  Creates a list of cohorts, given classroom list.
                   NOTE: This currently resets the cohort list after being called,
                   but really shouldn't. This is to accomodate for how this is
                   is implemented in mainWindow.py.
_reset_classrooms() - Resets classroom list (emptys students and sets to not in use)
_check_room_combo() - Checks the room combo being presented, returns combo if valid,
                      returns None if not.
most_even_rooms()   - Retrieves a list of the most even room distribution possible
divide_to_cohorts() - Reads the information in each classroom into a cohort, and returns
                      the list of cohorts.
"""
class Students:
    '''
    Description: this class will input students for each program and create
    appropriate cohorts. It will be implemented into the GUI app.
    '''
    def __init__(self):
        # initialize attributes
        self._BCOMStudents = 0
        self._PCOMStudents = 0

        self._PMStudents = 0
        self._BAStudents = 0
        self._SCMTStudents = 0
        self._FSStudents = 0
        self._DXDStudents = 0
        self._BKStudents = 0

        self._term = 0

        self._rooms = getClassrooms()
 
        """
        with open("data/classrooms.csv", "r") as file:
            # Read each line into a list with no newline character
            rooms_data = [l.strip() for l in file if "sep=" not in l]
            for room in rooms_data:
                name, cap = room.split(",")[0], int(room.split(",")[1])
                self._rooms.append(Classroom(name, cap))

        """
        # sort rooms by largest to smallest
        self._rooms = sorted(self._rooms, key=lambda x:x.normalCapacity, reverse=True)

    def cohorts_final(self):
        '''
        Description: this function will call divide_to_cohorts() and append
        the results to a list
        Returns: a list of lists of all the cohorts
        '''
        cohortList = []
        cohortList.append(self.divide_to_cohorts(self._PCOMStudents, "PC"))
        cohortList.append(self.divide_to_cohorts(self._BCOMStudents, "BC"))

        self._reset_classrooms(self._rooms)

        cohortList.append(self.divide_to_cohorts(self._PMStudents, "PM"))
        cohortList.append(self.divide_to_cohorts(self._BAStudents, "BA"))
        cohortList.append(self.divide_to_cohorts(self._SCMTStudents, "SCMT"))
        cohortList.append(self.divide_to_cohorts(self._BKStudents, "BK"))
        cohortList.append(self.divide_to_cohorts(self._FSStudents, "FS"))
        cohortList.append(self.divide_to_cohorts(self._DXDStudents, "DXD"))

        self._reset_classrooms(self._rooms)

        return cohortList

    def _reset_classrooms(self, classroom_list):
        for room in classroom_list:
            room.currentStudents = room.normalCapacity
            room.inUse = False
    
    def _check_space(self, combo, students):
        
        # If there are more students than space, this will return a negative
        # representing space needed, and if more space than students will
        # return space in room
        total_space = sum(classroom.normalCapacity for classroom in combo)
        return total_space - students
        
    def iterate_classrooms(self, students):
        
        empty_classrooms = [room for room in self._rooms if not room.inUse]
        
        # This variable name is a bit misleading, so it deserves
        # an explanation. 
        # We will be iterating through every combination of classrooms
        # using itertools.combination, and room_count represents
        # how many rooms are being added to the combination.
        room_count = 2
        classrooms_with_remaining_space = []
        for combo in itertools.combinations(empty_classrooms, room_count):
            students_copy = students
            smallest = min(combo, key=lambda x:x.normalCapacity)
            
            # Fits in room in this scenario
            if (value := self._check_space(combo, students_copy)) <= 0:
                classrooms_with_remaining_space.append([combo, value])

    def divide_to_cohorts(self, students, program):
        '''
        Description: this function will assign the appropriate prefix and
        divide by cohort size and return a list
        Returns: a list of cohort strings
        '''

        cohorts = []
        # Example entry: "PM0101: 11-533, 38/40

        num = 1

        # If there are no students, return the cohorts, as no cohorts can
        # be created.
        if students == 0:
            return cohorts

        rooms = self.most_even_rooms(students)

        if type(rooms) == str:
            print(f"{rooms} in {program}")
            quit()

        if rooms:
            for room in rooms:
                temp = Cohort(room, f"{program}{self._term:02d}{num:02d}", room.currentStudents)
                cohorts.append(temp)
                num += 1

        return cohorts
