'''
Author: Fahad Ali
Student ID: 3099218
Description: Create main GUI app, with multiple functionalities
References: 
https://www.geeksforgeeks.org/pyqt5-input-dialog-python/
https://www.pythonguis.com/tutorials/pyqt-dialogs/
'''
import sys
import Students

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    '''
    Description: This is the main window of the app, it will have buttons
    that have different dialogs for each UI element
    '''
    # main window class
    def __init__(self, parent = None):
        # initialize main window
        # super().__init__()
        super (MainWindow, self).__init__(parent)
        self.resize(600, 400)
        self.setWindowTitle("Schedule")
        self.setupUI()
        
    def cohort_button(self):
        # create cohort dialog and open it
        cohortDialog = CreateCohortDialog(self)
        cohortDialog.open()
        
    def schedule_button(self):
        # create schedule dialog and open it
        scheduleDialog = ScheduleDialog()
        scheduleDialog.open()
        
    def setupUI(self):
        # create layout for main window
        mainlLayout = QHBoxLayout(self)
        
        # create cohort button and execute dialog
        cohortButton = QPushButton("Click to Setup Cohorts", self)
        cohortButton.clicked.connect(self.cohort_button)
        
        #TODO: make scheudule functionality and dialog
        scheduleButton = QPushButton("Click to see Schedules", self)
        scheduleButton.clicked.connect(self.schedule_button)
        
        # add buttons to main window layout
        mainlLayout.addWidget(cohortButton, 1)
        mainlLayout.addWidget(scheduleButton, 1)
        # set main window layout
        self.setLayout(mainlLayout)

class CreateCohortDialog(QDialog):
    '''
    Description: This is the cohort dialog class, it will ask for input of the term
    and students in each program and output the cohorts
    '''
    def __init__(self, parent):
        # initialize the window
        super(CreateCohortDialog, self).__init__(parent)
        self.resize(500, 400)
        self.form = QGroupBox("Cohort")

        # creating a line edit texts for each program and set integer parameters
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 999)

        # create spin box for term number
        self.term = QSpinBox()
        self.term.setMaximum(3)
        self.term.setMinimum(1)

        # create text edit box that will only take integer numbers
        self.PCOM = QLineEdit()
        self.PCOM.setValidator(onlyInt)
        self.BCOM = QLineEdit()
        self.BCOM.setValidator(onlyInt)
        self.PM = QLineEdit()
        self.PM.setValidator(onlyInt)
        self.BA = QLineEdit()
        self.BA.setValidator(onlyInt)
        self.GLM = QLineEdit()
        self.GLM.setValidator(onlyInt)
        self.FS = QLineEdit()
        self.FS.setValidator(onlyInt)
        self.DXD = QLineEdit()
        self.DXD.setValidator(onlyInt)
        self.BK = QLineEdit()
        self.BK.setValidator(onlyInt)
        self.SCM = QLineEdit()
        self.SCM.setValidator(onlyInt)

        # call method that inputs numbers from the entry box
        self.setup_input()

        # creating a dialog button for save and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        
        # create cohort show button
        cohortShow = QPushButton("Click to see cohorts (please save first!)")
        
        # add functionality when "Cancel" clicked
        self.buttonBox.rejected.connect(self.reject)
        # add functionality when "Save" clicked
        self.buttonBox.accepted.connect(self.create_cohorts)
        
        ''' TODO: add dialog that gives error when save not clicked first
        # if self.buttonBox.accepted:
        # add functionality when "Clicked to show cohort" after saving
        cohortShow.clicked.connect(self.display_cohorts)
        # else:
        #     pass
        '''
        cohortShow.clicked.connect(self.display_cohorts)
        
        # create a veritcal layout in cohort dialog
        cohortLayout = QVBoxLayout()
        cohortLayout.addWidget(self.form)
        # add button to the cohort layout
        cohortLayout.addWidget(self.buttonBox)
        cohortLayout.addWidget(cohortShow)
        # set cohort lay out
        self.setLayout(cohortLayout)

    def create_cohorts(self):
        # call students class from students module
        self._studentCohort = Students.students()

        # assign input to class attributes
        self._studentCohort._term = int(self.term.text())
        self._studentCohort._BCOMStudents = int(self.BCOM.text())
        self._studentCohort._PCOMStudents = int(self.PCOM.text())
        self._studentCohort._PMStudents = int(self.PM.text())
        self._studentCohort._BAStudents = int(self.BA.text())
        self._studentCohort._GLMStudents = int(self.GLM.text())
        self._studentCohort._FSStudents = int(self.FS.text())
        self._studentCohort._DXDStudents = int(self.DXD.text())
        self._studentCohort._BKStudents = int(self.BK.text())
        self._studentCohort._SCMStudents = int(self.SCM.text())

        # create cohort final attribute
        self._cohortFinal = self._studentCohort.cohorts_final()

        return self._cohortFinal

    def display_cohorts(self):
        # create cohort table object
        CohortTable(self)

    def setup_input(self):
        # create a form layout for the cohort inputs
        studentInput = QFormLayout()

        studentInput.addRow(QLabel("Select term number: "), self.term) 
        studentInput.addRow(QLabel("Business Communication (BCOM)"), self.BCOM)
        studentInput.addRow(QLabel("Professional Communication (PCOM)"), self.PCOM)
        studentInput.addRow(QLabel("Project Management (PM)"), self.PM) 
        studentInput.addRow(QLabel("Business Analysis (BA)"), self.BA) 
        studentInput.addRow(QLabel("Global Logistics Management (GLM)"), self.GLM) 
        studentInput.addRow(QLabel("Full Stack Web Development (FS)"), self.FS) 
        studentInput.addRow(QLabel("Digital Experience Design Foundation (DXD)"), self.DXD) 
        studentInput.addRow(QLabel("BookKeeping Certificate (BK)"), self.BK) 
        studentInput.addRow(QLabel("Supply Chain Management (SCM)"), self.SCM) 

        # set the layout
        self.form.setLayout(studentInput)

class CohortTable(QWidget):
    '''
    Description: This class creates a table of the cohort groups
    '''
    def __init__(self, CreateCohortDialog):
        # inherit cohort dialog
        super().__init__(CreateCohortDialog)
        # set attributes
        self.table = QTableWidget()
        self.table.setColumnCount(len(CreateCohortDialog._cohortFinal))
        self.table.setRowCount(len(max(CreateCohortDialog._cohortFinal,key=len)))
        self.table.setHorizontalHeaderLabels(["BCOM", "PCOM", "PM", "BA", "GLM"\
            ,"FS", "DXD", "BK", "SCM"])
        self.table.resize(500,500)
        
        # initialize variables
        j = 0
        for cohortLists in CreateCohortDialog._cohortFinal:
            i = 0
            for cohorts in cohortLists:
                self.table.setItem(i, j, QTableWidgetItem(cohorts))
                i += 1
            j += 1
        
        self.table.show()

class ScheduleDialog(QDialog):
    # TODO: add schedules
    def __init__(self):
        # initialize the window
        super().__init__()
        self.resize(500, 400)

def main():
    pyqtRemoveInputHook()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()