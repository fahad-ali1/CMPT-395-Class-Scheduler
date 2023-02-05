"""
Author: Mike Lee
ID: 3067768
Date: 01/02/2023
Purpose: Rough idea of a classroom structure
"""

class Classroom:

    def __init__(self, classRoomNumber = '', normalCapacity = 0, lab = False):
        self.classRoomNumber = classRoomNumber
        self.normalCapacity = normalCapacity
        self.timeSlot = 0
        self.lab = lab
        self.isGhost = False


    def setGhost(self):
        self.isGhost = True

        
    def printClassroom(self):
        print("Classroom #: ", self.classRoomNumber, "Normal Capacity: ", self.normalCapacity,\
              "Time Slot: ", self.timeSlot, "lab: ", self.lab)

