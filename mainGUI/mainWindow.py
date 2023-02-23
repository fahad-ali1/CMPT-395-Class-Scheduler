'''
Author: Fahad Ali
Description: Create main GUI app, with multiple functionalities
'''

from PyQt5.QtWidgets import *
from PyQt5 import uic

import Students
import sys
import MikeCode

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()

        # Load the UI file
        uic.loadUi("MainWindow.ui", self)

        # call students class from students module
        self._studentCohort = Students.students()
        # Define student inputs (in student input tab)
        self.terminput = self.findChild(QSpinBox, "TermInput")
        self.BCOMinput = self.findChild(QSpinBox, "BCOMinput")
        self.PCOMinput = self.findChild(QSpinBox, "PCOMinput")
        self.PMinput = self.findChild(QSpinBox, "PMinput")
        self.BAinput = self.findChild(QSpinBox, "BAinput")
        self.SCMTinput = self.findChild(QSpinBox, "SCMTinput")
        self.BKinput = self.findChild(QSpinBox, "BKinput")
        self.FSinput = self.findChild(QSpinBox, "FSinput")
        self.DXDinput = self.findChild(QSpinBox, "DXDinput")
        
        # Define buttons in input tab
        self.createCohort = self.findChild(QPushButton, "CreateCohort")
        self.revertButton = self.findChild(QPushButton, "RevertButton")
        self.uploadButton = self.findChild(QPushButton, "UploadFileButton")
        
        # Define cohorts tables in cohort tab
        self.cohortTable1 = self.findChild(QTableWidget, "CohortTable1")
        self.cohortTable2 = self.findChild(QTableWidget, "CohortTable2")
        self.cohortTable3 = self.findChild(QTableWidget, "CohortTable3")

        # Define buttons in cohort tab 
        self.saveAs = self.findChild(QPushButton, "SaveAsCohort")
        
        # Call revert_changes function 
        self.revertButton.clicked.connect(self.revert_changes)

        # Open file browser if upload file clicked
        self.uploadButton.clicked.connect(self.upload_file)

        #test
        self.createCohort.clicked.connect(self.create_cohorts)
        self.createCohort.clicked.connect(self.add_cohort_table)

    def create_cohorts(self):
        '''
        Description: assign input to students class to create cohorts
        '''        
        # assign input to class attributes
        self._studentCohort._term = int(self.terminput.text())
        self._studentCohort._BCOMStudents = int(self.BCOMinput.text())
        self._studentCohort._PCOMStudents = int(self.PCOMinput.text())
        self._studentCohort._PMStudents = int(self.PMinput.text())
        self._studentCohort._BAStudents = int(self.BAinput.text())
        self._studentCohort._SCMTStudents = int(self.SCMTinput.text())
        self._studentCohort._BKStudents = int(self.BKinput.text())
        self._studentCohort._FSStudents = int(self.FSinput.text())
        self._studentCohort._DXDStudents = int(self.DXDinput.text())

        # create cohort final attribute
        self._cohortFinal = self._studentCohort.cohorts_final()

    def add_cohort_table(self):
        '''
        Description: create cohort tables
        '''
        self.tables = [self.cohortTable1, self.cohortTable2, self.cohortTable3]
        self.tables[int(self.terminput.text())-1].setRowCount(len(max(self._cohortFinal,key=len)))
        
        j = 0
        for cohortLists in self._cohortFinal:
            i = 0
            for cohorts in cohortLists:
                self.tables[int(self.terminput.text())-1].setItem(i, j, QTableWidgetItem(cohorts))
                i += 1
            j += 1
    
    def revert_changes(self):
        '''
        Description: revert all changes 
        '''
        for tables in range (1,4):
        # Set all spin box objects to 0
            self.terminput.setValue(tables)
            self.BCOMinput.setValue(0)
            self.PCOMinput.setValue(0)
            self.PMinput.setValue(0)
            self.BAinput.setValue(0)
            self.SCMTinput.setValue(0)
            self.BKinput.setValue(0)
            self.FSinput.setValue(0)
            self.DXDinput.setValue(0)

            # Delete all cohorts and information on the cohort tables
            self.create_cohorts()
            self.add_cohort_table()
            
        self.terminput.setValue(0)
        
    def upload_file(self):
        '''
        Description: open dialog box to select file
        '''
        # open file browser to choose file
        path = QFileDialog.getOpenFileName()
        # give path 
        filename = path[0]
        
        #in testing
        fileinput = MikeCode.getProgramNumbers(filename)
        #in testing
        print(fileinput[0])

# Initialize The App
def main():
    app = QApplication(sys.argv)
    UIWindow = MainMenu()
    UIWindow.show()
    app.exec()