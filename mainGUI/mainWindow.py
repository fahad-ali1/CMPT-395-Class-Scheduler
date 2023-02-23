'''
Author: Fahad Ali
Description: Create main GUI app, with multiple functionalities
'''

from PyQt5.QtWidgets import *
from PyQt5 import uic

import Students
import sys

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
        self.GLMinput = self.findChild(QSpinBox, "GLMinput")
        self.FSinput = self.findChild(QSpinBox, "FSinput")
        self.DXDinput = self.findChild(QSpinBox, "DXDinput")
        self.BKinput = self.findChild(QSpinBox, "BKinput")
        self.SCMinput = self.findChild(QSpinBox, "SCMinput")
        
        # Define buttons in input tab
        self.saveButton = self.findChild(QPushButton, "CreateCohort")
        self.revertButton = self.findChild(QPushButton, "RevertButton")
        self.uploadButton = self.findChild(QPushButton, "UploadFileButton")
        
        # Define cohorts table in cohort tab
        self.cohortTable = self.findChild(QTableWidget, "CohortTable")
        
        # Define buttons in cohort tab 
        self.saveAs = self.findChild(QPushButton, "SaveAsCohort")
        
        # Call revert_changes function 
        self.revertButton.clicked.connect(self.revert_changes)

        # Open file browser if upload file clicked
        self.uploadButton.clicked.connect(self.upload_file)

        #test
        self.saveButton.clicked.connect(self.create_cohorts)
        self.saveButton.clicked.connect(self.add_cohort_table)

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
        self._studentCohort._GLMStudents = int(self.GLMinput.text())
        self._studentCohort._FSStudents = int(self.FSinput.text())
        self._studentCohort._DXDStudents = int(self.DXDinput.text())
        self._studentCohort._BKStudents = int(self.BKinput.text())
        self._studentCohort._SCMStudents = int(self.SCMinput.text())

        # create cohort final attribute
        self._cohortFinal = self._studentCohort.cohorts_final()

    def add_cohort_table(self):
        '''
        Description: create cohort table
        '''
        self.cohortTable.setRowCount(len(max(self._cohortFinal,key=len)))
        
        j = 0
        for cohortLists in self._cohortFinal:
            i = 0
            for cohorts in cohortLists:
                self.cohortTable.setItem(i, j, QTableWidgetItem(cohorts))
                i += 1
            j += 1
    
    def revert_changes(self):
        '''
        Description: revert all changes 
        '''
        # Set all spin box objects to 0
        self.terminput.setValue(1)
        self.BCOMinput.setValue(0)
        self.PCOMinput.setValue(0)
        self.PMinput.setValue(0)
        self.BAinput.setValue(0)
        self.GLMinput.setValue(0)
        self.FSinput.setValue(0)
        self.DXDinput.setValue(0)
        self.BKinput.setValue(0)
        self.SCMinput.setValue(0)

        # Delete all cohorts and information on the cohort table
        self.create_cohorts()
        self.add_cohort_table()
        
    def upload_file(self):
        '''
        Description: open dialog box to select file
        '''
        # open file browser to choose file
        path = QFileDialog.getOpenFileName()
        # give path 
        self.file = path[0]

# Initialize The App
def main():
    app = QApplication(sys.argv)
    UIWindow = MainMenu()
    UIWindow.show()
    app.exec()