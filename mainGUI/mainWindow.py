'''
Author: Fahad Ali
Description: Create main GUI app, with multiple functionalities
'''

from PyQt5.QtWidgets import *
from PyQt5 import uic

import Students
import sys
import MikeCode

class MainMenu(QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()

        # Load the UI file
        uic.loadUi("MainWindow.ui", self)

        # call students class from students module
        self._studentCohort = Students.students()
        
        # list to zero all the spin boxes quickly
        self.zero = [0,0,0,0,0,0,0,0]
        
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
        self.revertButton2 = self.findChild(QPushButton, "RevertButton2")
        self.uploadButton = self.findChild(QPushButton, "UploadFileButton")
        self.uploadButton2 = self.findChild(QPushButton, "UploadFileButton2")
        
        # Define cohorts tables in cohort tab
        self.cohortTable1 = self.findChild(QTableWidget, "CohortTable1")
        self.cohortTable2 = self.findChild(QTableWidget, "CohortTable2")
        self.cohortTable3 = self.findChild(QTableWidget, "CohortTable3")

        # Define buttons in cohort tab 
        self.saveAs = self.findChild(QPushButton, "SaveAs")
        self.saveAs2 = self.findChild(QPushButton, "SaveAs2")
        
        # Call revert_changes function 
        self.revertButton.clicked.connect(self.revert_changes)
        self.revertButton2.clicked.connect(self.revert_changes)
        
        # Open file browser if upload file clicked
        self.uploadButton.clicked.connect(self.upload_file)
        self.uploadButton2.clicked.connect(self.upload_file)

        # Create cohorts when button clicked
        self.createCohort.clicked.connect(self.create_cohorts)
        self.createCohort.clicked.connect(self.add_cohort_table)
    
        # Save cohorts as .xlsc file
        self.saveAs.clicked.connect(self.save_as)
        self.saveAs2.clicked.connect(self.save_as)
        
    def spin_box_values(self, value, tables):
            '''
            Description: changes spinbox values
            '''
            # set value of each box to a certain value
            self.terminput.setValue(tables)
            self.BCOMinput.setValue(value[0])
            self.PCOMinput.setValue(value[1])
            self.PMinput.setValue(value[2])
            self.BAinput.setValue(value[3])
            self.SCMTinput.setValue(value[4])
            self.BKinput.setValue(value[5])
            self.FSinput.setValue(value[6])
            self.DXDinput.setValue(value[7])

    def revert_changes(self):
        '''
        Description: revert all changes 
        '''
        for tables in range (1,4):
            # Set all spin box objects to 0
            self.spin_box_values(self.zero, tables)

            # Delete all cohorts and information on the cohort tables
            self.create_cohorts()
            self.add_cohort_table()
        # return to default value
        self.terminput.setValue(1)

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
        # assign variables
        self.tables = [self.cohortTable1, self.cohortTable2, self.cohortTable3]
        self.tables[int(self.terminput.text())-1].setRowCount(len(max(self._cohortFinal,key=len)))
        j = 0
        
        # create cells for each table and add information
        for cohortLists in self._cohortFinal:
            i = 0
            for cohorts in cohortLists:
                self.tables[int(self.terminput.text())-1].setItem(i, j, QTableWidgetItem(cohorts))
                i += 1
            j += 1
            
    def upload_file(self):
        '''
        Description: open dialog box to select file and then auto input all 
        students into cohorts and create schedule for each room
        '''
        # open file browser to choose file
        path = QFileDialog.getOpenFileName()
        
        # give path if the user does not hit cancel 
        if path:
            filename = path[0]
            try:
                # input file and extract student inputs
                fileinput = MikeCode.getProgramNumbers(filename)

                studentsByProgarm = {"BCOM":fileinput[0], "PCOM":fileinput[1], 
                                    "PM":fileinput[2], "BA":fileinput[3], 
                                    "SCMT":fileinput[4], "BK":fileinput[5],
                                    "FS":fileinput[6], "DXD":fileinput[7]}
                term1=[]
                term2=[]
                term3=[]
                inputs = [term1, term2, term3]
                
                # loop through dictionary values
                for studentInputs in studentsByProgarm.values():
                    # studentInputs[0] = term 1
                    # studentInputs[1] = term 2
                    # studentInputs[2] = term 3
                    term1.append(int(studentInputs[0]))
                    term2.append(int(studentInputs[1]))
                    term3.append(int(studentInputs[2]))
                    
                # assign and create cohorts in the tables from the file 
                for tables in range (1,4):
                    self.spin_box_values(inputs[tables-1], tables)

                    self.create_cohorts()
                    self.add_cohort_table()
                    
                self.spin_box_values(self.zero, tables)
                self.terminput.setValue(1)
            # if user hits cancel, error will not crash the app
            except:
                pass
    
    def save_as(self):
        '''
        Description: saves any of the tables as .xlsx files for microsoft excel
        '''
        ###################### TODO: In development
        path = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        
# Initialize The App
def main():
    app = QApplication(sys.argv)
    UIWindow = MainMenu()
    UIWindow.show()
    app.exec()