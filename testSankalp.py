from lib.courses import *

fileNameTester = "CourseTester.xlsx"
courseNameTester = ["PCOM 0204", "SUPR 0841", "PCOM 0t04"]
courseLocation = []
newInfo = ["DXDI 9901",	"DXD Capstone", "45", "Lab", "", "", "", ""]
oldInfo = ["PCOM 0204", "Business Persuasion and Research", "35", "", "", "", "", ""]

def pause():

    input("Press Enter...")

if __name__ == "__main__":

    print("\nSankalp Testing\n")

    # get courses
    for i in range(len(courseNameTester)):
        course_id = getCourse(fileNameTester, courseNameTester[i])

        if course_id != None: courseLocation.append(course_id)
        # print(course_id)

    # print(courseLocation)

    #showcase changeFunction
    print("Change info")
    changeCourseInfo(courseLocation[0], newInfo, fileNameTester)
    pause()
    print("Revert info")
    changeCourseInfo(courseLocation[0], oldInfo, fileNameTester)