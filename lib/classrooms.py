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
timeBlocks      - List of time blocks to represent a rooms schedule
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
        self.classRoomNumber = classRoomNumber.strip()
        self.normalCapacity = normalCapacity
        self.currentStudents = normalCapacity
        self.currentBlockTime = None
        self.lab = lab
        self.inUse = False
        self.isGhost = False
        self.noSpaceForBlocks = False
        self.timeBlocks = []
        
    def __repr__(self):
        return f"Classroom(name={self.classRoomNumber}, cap={self.normalCapacity})"

    def setGhost(self):
        self.isGhost = True

    def setBlockTime(self, time):
        self.currentBlockTime = time

    def addBlock(self, newTimeBlock):
        self.timeBlocks.append(newTimeBlock)

    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity, \
              "lab: ", self.lab, " isGhost: ", self.isGhost)

