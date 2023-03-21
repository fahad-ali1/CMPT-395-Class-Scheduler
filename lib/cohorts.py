# Authors: Mike, Schuyler
# Purpose:
#   Module centerd around creating cohorts, based on existing classrooms.


import math, itertools


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
        self.programCourses = []  # program class

    def __repr__(self):
        return f"{self.cohortName} - {self.classroom.classRoomNumber}, {self.size}/{self.classroom.normalCapacity}"


"""
CLASSROOM
---------

ATTRIBUTES
----------
classRoomNumber - Number of room (i.e. 11-533)
normalCapacity  - Capacity of classroom
currentStudents - Current students occupying classroom.
                  NOTE: Set to max capacity at first, and is modified later
lab             - Boolean representing whether room is a lab or not
inUse           - Boolean representing whether room is in use or not
isGhost         - Boolean representing whether or not room is a ghost room

METHODS
-------
setGhost() - Changes a room into a ghost room
printClassroom() - Prints the classroom data
"""
class Classroom:
    def __init__(self, classRoomNumber='', normalCapacity=0, lab=False):
        self.classRoomNumber = classRoomNumber
        self.normalCapacity = normalCapacity
        self.currentStudents = normalCapacity
        self.lab = lab
        self.inUse = False
        self.isGhost = False

    def setGhost(self):
        self.isGhost = True

    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity, \
              "lab: ", self.lab, " isGhost: ", self.isGhost)


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

        self._rooms = []
        with open("data/classrooms.csv", "r") as file:
            # Read each line into a list with no newline character
            rooms_data = [l.strip() for l in file if "sep=" not in l]
            for room in rooms_data:
                name, cap = room.split(",")[0], int(room.split(",")[1])
                self._rooms.append(Classroom(name, cap))

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


    def _check_room_combo(self, temp, combo, percent, wiggle_percent):

        # Iterate through each room in the combo
        for room in combo:
            wiggle_room = math.floor(room.normalCapacity - (room.normalCapacity * wiggle_percent))
            allowed_total = math.floor(room.normalCapacity - (room.normalCapacity * percent))

            # If the remaining students is less than the allowed total, return, as
            # this combination simply will not work.
            if temp - wiggle_room < 0:
                return None
            # Handle if the remaining students can reasonably fit into the room.

            if temp - wiggle_room >= 0:

                # Check conditions for if this room combo is acceptable.
                if room == combo[-1] and wiggle_room <= temp <= room.normalCapacity:
                    room.currentStudents = temp
                    return combo

                # Convert to int, as allowed total will be a float with ?.0 in it
                room.currentStudents = int(allowed_total)
                temp -= allowed_total
                if temp == 0:
                    return combo

    def most_even_rooms(self, students):

        empty_classrooms = []
        for room in self._rooms:
            if not room.inUse:
                empty_classrooms.append(room)

        if not empty_classrooms:
            return f"Need room for {students} students"

        percent = 0.05
        wiggle_room = 0.05
        result_found = False
        being_compared = 1
        while not result_found:
            for combo in itertools.combinations(empty_classrooms, being_compared):
                combo = list(combo)
                temp = students

                # Reset classrooms so that the state of classrooms is
                # identical for each check.
                # NOTE: I really don't know if this is necessary, it just
                #       eliminates the possibility of bugs.
                self._reset_classrooms(combo)
                combo_result = self._check_room_combo(temp, combo, percent, wiggle_room)

                if combo_result:
                    # Make the result mutable
                    combo_result = list(combo_result)

                    for result in combo_result:
                        result.in_use = True
                    return combo_result

            being_compared += 1

            # If being compared is 5, increase percent and reset combo value
            if being_compared == len(empty_classrooms) + 1:

                # Set conditions as a series of gates

                # If the percent is zero, start adjusting the wiggle room
                # that the final classroom can fit within
                if percent == 0:
                    if wiggle_room < 1:
                        wiggle_room += 0.01
                    else:
                        wiggle_room = 1

                # If the percentage isn't zero, reduce how much room should
                # remain in the classrooms
                if percent != 0:
                    percent -= 0.01
                    if percent < 0:
                        percent = 0

                being_compared = 1

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

