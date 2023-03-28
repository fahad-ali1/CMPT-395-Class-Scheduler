# Class Scheduler
Scheduler assignment for CMPT 395. Will create a schedule for MacEwan's department of continuing education.

### Author(s)
 - Fahad Ali (GUI)
 - Schuy (Cohorts)
 - Mike (Scheduling and related data structures)
 - Sankalp (Changing course info in xlsx file)
 
 ## Installation
 If you have python3 installed (you can install python [here.](https://www.python.org/downloads/)\) Otherwise, download the `.exe` file under the releases section (W.I.P.).
 
 ## Dependencies
 Currently, the project is dependent on [PyQt5](https://pypi.org/project/PyQt5/) and [openpyxl](https://pypi.org/project/openpyxl/)\. You can install these by running:
 ```
 pip install PyQt5 openpyxl
 ```
 Please note that these dependencies aren't necessary if you download and run the `.exe` version.
 
 ## How To Run
 As stated above, please make sure you have both `PyQt5` and `openpyxl` packages installed. Besides that, all you need to do is either double click the `main.py` file or run the following terminal command in Powershell:
 ```
 python main.py
 ```
 
 ## Testing
 The tests require that you are on a Windows machine. They only depend on `python` and `openpyxl`, so as long as both are installed, the tests can be ran. You can run the tests by calling
 ```
 Tests/run_all.bat
 ```
 From the root directory of the project. This will run all automated tests that it can, and will create log files for any tests we felt needed to be tested by inspection. You can also run each test individually by running
 ```
 python -m Tests.<test_name>
 ```
 where `<test_name>` is the name of the test file in the `Tests` directory.
 
