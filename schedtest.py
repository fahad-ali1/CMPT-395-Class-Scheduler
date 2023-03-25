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
week = Week(0)
def scheduleCourses(week, cohorts):
    for cohort in cohorts:
        courseQueue = deque(cohort.program.term1)

        if "BCOM" in cohort.name or "PCOM" in cohort.name:
            days = [week.getDay("Monday"), week.getDay("Wednesday")]
        else:
            days = [week.getDay("Tuesday"), week.getDay("Thursday")]

        while courseQueue:
            currentCourse = courseQueue.popleft()
            prefClassroomName = cohort.clasroom.classRoomNumer
            day1 = days[0]
            day2 = days[1]
            for i in range(0, len(week.days.classrooms)):
                if (prefClassroomName == day1.classrooms[i] and day1.classrooms[i].inUse is False) and \
                   (prefClassroomName == day2.classrooms[i] and day2.classrooms[i].inUse is False):
                    startTime, endTime = scheduleLecture(currentCourse.lecturelength,
                                                         week.days.classrooms[i].currentBlockTime)
                    newBlock = timeBlock(startTime, endTime, cohort.cohortname, currentCourse.courseName, 0, 0)
                    day1.classrooms[i].timeBlocks.append(newBlock)
                    day2.classrooms[i].timeBlocks.append(newBlock)
    return copy.deepcopy(week)


