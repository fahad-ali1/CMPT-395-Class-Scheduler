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
        print(f"{cohort.cohortName} - {cohort.classroom.classRoomNumber}")
        courseQueue = deque(cohort.programCourses.term1)

        if "BC" in cohort.cohortName or "PC" in cohort.cohortName:
            days = [week.getDay("Monday"), week.getDay("Wednesday")]
        else:
            days = [week.getDay("Tuesday"), week.getDay("Thursday")]

        while courseQueue:
            currentCourse = courseQueue.popleft()
            prefClassroomName = cohort.classroom.classRoomNumber
            for day in days:
            
                scheduled_preferred_room = False
                for i in range(0, len(day.classrooms)):
                    # Create new time block for iteration. Values can be discarded if not used
                    if (return_value := scheduleLecture(currentCourse.lectureLength, day.classrooms[i].currentBlockTime)) == "-2":
                        continue
                    else:
                        startTime, endTime = return_value

                    newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)
                    
                    if day.classrooms[i].available_at_time(startTime, endTime):
                        if day.classrooms[i].classRoomNumber == prefClassroomName and cohort.size <= day.classrooms[i].normalCapacity:
                            day.classrooms[i].timeBlocks.append(newBlock)
                            day.classrooms[i].currentBlockTime = endTime
                            scheduled_preferred_room = True
                            break
                            
                    
                if not scheduled_preferred_room:
                    for i in range(0, len(day.classrooms)):
                    
                        # Create new time block for iteration. Values can be discarded if not used
                        startTime, endTime = scheduleLecture(currentCourse.lectureLength, day.classrooms[i].currentBlockTime)
                        newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)
                        
                        # Store the first class found in the first iteration.
                        if day.classrooms[i].available_at_time(startTime, endTime):
                            if cohort.size <= day.classrooms[i].normalCapacity:
                                day.classrooms[i].timeBlocks.append(newBlock)
                                day.classrooms[i].currentBlockTime = endTime
                                break

        return copy.deepcopy(week)