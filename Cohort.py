"""
Author: Sankalp Shrivastav
ID: 3106374
Date: 02/02/2023
Purpose: A basic idea for the Cohort data structure
"""

class Cohort:

    def __init__(self, name = "BA11", size = 20, lab = False) -> None:
        
        self._cohortName = name
        self._cohortSize = size
        self._isLab = lab
        self._courseFinished = []
        self._courseNotFinished = []
        self._timeTable = None
    
    def __str__(self) -> str:
        
        return  f"\nCohort: {self._cohortName}\n"\
                f"Size: {self._cohortSize}\n"\
                f"Courses Done: {self._courseFinished}\n"\
                f"Courses NotDone: {self._courseNotFinished}\n"
    
    def changeType(self, type = False) -> None:

        #change the type of class

        self._isLab = type

    def display(self) -> None:

        print(self)
    
    def updateSize(self, size):

        self._cohortSize = size
    
    def addToFinish(self, course):

        self._courseFinished.append(course)
    
    def addToNotFinish(self, course):

        self._courseNotFinished.append(course)
    
    def addTimeTable(self, timeTable):

        self._timeTable = timeTable

if __name__ == '__main__':

    print("Testing Cohort")

    cohort1 = Cohort()

    print(cohort1)