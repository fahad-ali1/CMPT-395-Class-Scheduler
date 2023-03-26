import copy
from collections import deque
from lib.scheduler import *
from lib.scheduler import scheduleLecture, timeBlock, createTemplateWeek
from lib.fileio import getClassrooms

'''def schedulerTest(cohortList, dayList):

    for cohort in cohortList:
        courses = cohort.program.getTerm1()
        while courses:
            currentCourse = courses.pop(0)
            lecLen = currentCourse.lectureLength
'''


def scheduleCourses(week, cohorts):
    for cohort in cohorts:
        courseQueue = deque(cohort.programCourses.term1)

        if "BC" in cohort.cohortName or "PC" in cohort.cohortName:
            days = [week.getDay("Monday"), week.getDay("Wednesday")]
        else:
            days = [week.getDay("Tuesday"), week.getDay("Thursday")]

        while courseQueue:
            currentCourse = courseQueue.popleft()
            prefClassroomName = cohort.classroom.classRoomNumber
            day1 = days[0]
            day2 = days[1]
            for day in [day1, day2]:
                for i in range(0, len(day.classrooms)):
                    if (prefClassroomName == day1.classrooms[i].classRoomNumber and day1.classrooms[i].inUse is False) and \
                       (prefClassroomName == day2.classrooms[i].classRoomNumber and day2.classrooms[i].inUse is False):

                        startTime, endTime = scheduleLecture(currentCourse.lectureLength, day.classrooms[i].currentBlockTime)
                        newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)

                        if checkIfAvailable(day.classrooms[i].timeBlocks, newBlock) != "nofit":
                            day.classrooms[i].timeBlocks.append(newBlock)
                            day.classrooms[i].currentBlockTime = endTime
                            break
        return copy.deepcopy(week)



def checkIfAvailable(timeBlocks, newBlock):
    for timeblock in timeBlocks:
        if newBlock.startTime == timeblock.startTime or newBlock.endTime == timeblock.endTime:
            return "nofit"
