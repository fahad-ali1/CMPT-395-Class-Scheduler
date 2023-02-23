'''
Author: Fahad Ali
Student ID: 3099218
Description: This program will create cohorts of the best size depending on 
the class space available, and suggest (if required) more class space
'''

class students:
    '''
    Description: this class will input students for each program and create
    appropriate cohorts. It will be implemented into the GUI app.
    '''
    def __init__(self):
        # initialize attributes
        self._BCOMStudents = None
        self._PCOMStudents = None

        self._PMStudents = None
        self._BAStudents = None
        self._SCMTStudents = None
        self._FSStudents = None
        self._DXDStudents = None
        self._BKStudents = None
        
        self._term = None

    def cohorts_final(self):
        '''
        Description: this function will call divide_to_cohorts() and append
        the results to a list
        Returns: a list of lists of all the cohorts
        '''
        cohortList = []
        cohortList.append(self.divide_to_cohorts(self._BCOMStudents, 0))
        cohortList.append(self.divide_to_cohorts(self._PCOMStudents, 1))

        cohortList.append(self.divide_to_cohorts(self._PMStudents, 2))
        cohortList.append(self.divide_to_cohorts(self._BAStudents, 3))
        cohortList.append(self.divide_to_cohorts(self._SCMTStudents, 4))
        cohortList.append(self.divide_to_cohorts(self._BKStudents, 5))
        cohortList.append(self.divide_to_cohorts(self._FSStudents, 6))
        cohortList.append(self.divide_to_cohorts(self._DXDStudents, 7))

        return(cohortList)

    def divide_to_cohorts(self, students, ID):
        '''
        Description: this function will assign the appropriate prefix and 
        divide by cohort size and return a list
        Returns: a list of cohort strings
        '''
        # initialize values
        cohortDict = {0:"BC", 1: "PC", 2:"PM", 3:"BA", 4:"SCMT", 5:"BK", 6:"FS",\
                      7:"DXD"}
        cohortProgramList = []
        cohortGroups = 0
        studentRemaining = 0
        cohortSize = 30 # change to whatever size cohort is needed

        # loop through students in a program
        for student in range(students):
            studentRemaining = students
            # put into cohort groups
            if student % cohortSize == 0: 
                cohortGroups += 1
                studentRemaining -= student
                # proper name convention 
                if cohortGroups < 10:
                    cohortProgramList.append(f"{cohortDict.get(ID)}0{self._term}0{cohortGroups}") 
                elif cohortGroups < 20:
                    cohortProgramList.append(f"{cohortDict.get(ID)}1{self._term}1{cohortGroups}") 
                    
            if studentRemaining <= 25:
                # TODO: average out the cohorts if moer than 1 cohort is made 
                # and the last cohort is under 25 people
                pass

        return (cohortProgramList)