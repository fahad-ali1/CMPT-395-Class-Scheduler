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
        self.saveButton = self.findChild(QPushButton, "SaveButton")
        self.revertButton = self.findChild(QPushButton, "RevertButton")
        self.uploadButton = self.findChild(QPushButton, "UploadFileButton")
        
        # Define cohorts table (in cohorts tab)
        self.cohortTable = self.findChild(QTableWidget, "CohortTable")
        
        # Define buttons in input tab 
        self.saveAs = self.findChild(QPushButton, "SaveAsCohort")

        #test
        self.saveButton.clicked.connect(self.create_cohorts)
        self.saveButton.clicked.connect(self.add_cohort_table)

    def create_cohorts(self):
        """
        Description: assign 
        """
        # call students class from students module
        self._studentCohort = Students.students()
        
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

        return self._cohortFinal

    def add_cohort_table(self):
        
        self.cohortTable.setRowCount(len(max(self._cohortFinal,key=len)))
        
        j = 0
        for cohortLists in self._cohortFinal:
            i = 0
            for cohorts in cohortLists:
                self.cohortTable.setItem(i, j, QTableWidgetItem(cohorts))
                i += 1
            j += 1
            
# Initialize The App
def main():
    app = QApplication(sys.argv)
    UIWindow = MainMenu()
    UIWindow.show()
    app.exec()

if __name__ == "__main__":
    main()