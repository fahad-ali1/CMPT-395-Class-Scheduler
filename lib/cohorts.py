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
        
    def _iterate_classrooms(self, students):
        
        empty_classrooms = [room for room in self._rooms if not room.inUse]
        
        # This variable name is a bit misleading, so it deserves
        # an explanation. 
        # We will be iterating through every combination of classrooms
        # using itertools.combination, and room_count represents
        # how many rooms are being added to the combination.
        room_count = 1
        
        # The two below variables exist explicitly for if students fill every
        # classroom. In the scenario, we want the students placed in classes in such
        # a way that the remaining students are as few as possible.
        max_remainder = None
        max_remainder_combo = None
        
        classrooms_with_remaining_space = []
        not_one_class_totally_empty = True
        ghost_rooms_not_needed = True
        while not_one_class_totally_empty and ghost_rooms_not_needed:
            for combo in itertools.combinations(empty_classrooms, room_count):
            
                # If the length of the combo reaches 1+ the total number of classrooms,
                # ghost rooms are needed, and we can break the loop.
                if len(combo) + 1 == len(empty_classrooms):
                    ghost_rooms_not_needed = False
                    continue
                
                smallest = min(combo, key=lambda x:x.normalCapacity)
                remainder = self._check_space(combo, students)
                
                if max_remainder is None or remainder > max_remainder:
                    max_remainder = remainder
                    max_remainder_combo = combo
                
                # If one class is completely empty, set the flag
                if remainder > smallest.normalCapacity:
                    not_one_class_totally_empty = False
                
                # Fits in room in this scenario
                elif 0 <= remainder <= smallest.normalCapacity:
                    classrooms_with_remaining_space.append([combo, remainder])
                    
            room_count += 1
        
        if ghost_rooms_not_needed:
            final_combo_choice = min(classrooms_with_remaining_space, key=lambda x: x[-1])
        else:
            final_combo_choice = [max_remainder_combo, max_remainder]
            
        return final_combo_choice
        
    def divide_to_cohorts(self, students, program):
        """
        Description: Will change the representation in the classroom combo into a meaningful
                     representation of a cohort (Aka list of cohorts)
        Params: students - number of students cohorts are being made out of.
        Returns: A list of cohort objects
        """
        
        available_rooms, remainder = self._iterate_classrooms(students)
        if remainder is None:
            any_rooms_available_in_the_first_place = False
        else:
            any_rooms_available_in_the_first_place = True
            
        if not any_rooms_available_in_the_first_place:
            uses_ghost_rooms = True
        else:   
            uses_ghost_rooms = remainder < 0
        
        cohorts = []
        
        if not uses_ghost_rooms:
            for i, room in enumerate(available_rooms):
                if students - room.normalCapacity >= 0:
                    room.currentStudents = room.normalCapacity
                    students -= room.normalCapacity
                else:
                    room.currentStudents = students
                room.inUse = True
                cohorts.append(Cohort(room, f"{program}{self._term:02d}{(i + 1):02d}", room.currentStudents))
        else:
            cohort_num = 0
            if any_rooms_available_in_the_first_place:
                cohorts_num = 1
                for i, room in enumerate(available_rooms):
                    cohort_num = i + 1
                    room.currentStudents = room.normalCapacity
                    students -= room.normalCapacity
                    room.inUse = True
                    cohorts.append(Cohort(room, f"{program}{self._term:02d}{(i + 1):02d}", room.currentStudents))
                
            # Begin appending ghost rooms here:
            cohort_num += 1
            room = min(self._rooms, key=lambda x: x.normalCapacity)
            room = Classroom("??-???", room.normalCapacity)
            while students - room.normalCapacity > 0:
                cohorts.append(Cohort(room, f"{program}{self._term:02d}{cohort_num:02d}", room.currentStudents))
                cohort_num += 1
                students -= room.normalCapacity
            room.currentStudents = students
            cohorts.append(Cohort(room, f"{program}{self._term:02d}{cohort_num:02d}", room.currentStudents))
            
        return cohorts
        

    """ 
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
    """