"""
Author: Mike Lee, Schuyler Kelly
Purpose: Classroom object, fixes circular import
"""


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

