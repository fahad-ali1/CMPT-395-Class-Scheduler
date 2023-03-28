import copy, random
from collections import deque
from lib.scheduler import *
from lib.scheduler import scheduleLecture, timeBlock, createTemplateWeek
from lib.fileio import getClassrooms


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
            lectureLength = currentCourse.lectureLength

            # Determine how many times to schedule the lecture
            if lectureLength == 1.5:
                schedule_days = days
            else:
                schedule_days = [random.choice(days)]

            for day in schedule_days:
            
                # If the preferred classroom is a ghost room, add it to the list of classrooms
                if prefClassroomName == "??-???" and cohort.classroom not in day.classrooms:
                    day.classrooms.append(cohort.classroom)

                scheduled_preferred_room = False
                for i in range(len(day.classrooms)):
                    if (return_value := scheduleLecture(lectureLength, day.classrooms[i].currentBlockTime)):
                        startTime, endTime = return_value
                    else:
                        continue

                    newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)
                    if day.classrooms[i].available_at_time(startTime, endTime):
                        if day.classrooms[i].classRoomNumber == prefClassroomName and cohort.size <= day.classrooms[i].normalCapacity:
                            day.classrooms[i].timeBlocks.append(newBlock)
                            day.classrooms[i].currentBlockTime = endTime
                            scheduled_preferred_room = True
                            break

                if not scheduled_preferred_room:
                    for i in range(len(day.classrooms)):
                        if (return_value := scheduleLecture(lectureLength, day.classrooms[i].currentBlockTime)):
                            startTime, endTime = return_value
                        else:
                            continue

                        newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)
                        if day.classrooms[i].available_at_time(startTime, endTime):
                            if cohort.size <= day.classrooms[i].normalCapacity:
                                day.classrooms[i].timeBlocks.append(newBlock)
                                day.classrooms[i].currentBlockTime = endTime
                                break

    return copy.deepcopy(week)


"""
def scheduleCourses(week, cohorts):

    for cohort in cohorts:
        
        print(cohort.cohortName, cohort.size)
        courseQueue = deque(cohort.programCourses.term1)

        if "BC" in cohort.cohortName or "PC" in cohort.cohortName:
            days = [week.getDay("Monday"), week.getDay("Wednesday")]
        else:
            days = [week.getDay("Tuesday"), week.getDay("Thursday")]

        while courseQueue:
            currentCourse = courseQueue.popleft()
            prefClassroomName = cohort.classroom.classRoomNumber
            for day in days:
                
                # If the preferred classroom is a ghost room, add it to the list of classrooms
                if prefClassroomName == "??-???":
                    day.classrooms.append(cohort.classroom)
                    
                scheduled_preferred_room = False
                for i in range(0, len(day.classrooms)):
                    # Create new time block for iteration. Values can be discarded if not used

                    if (return_value := scheduleLecture(currentCourse.lectureLength, day.classrooms[i].currentBlockTime)):
                        startTime, endTime = return_value
                    else:
                        continue

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
                        if (return_value := scheduleLecture(currentCourse.lectureLength, day.classrooms[i].currentBlockTime)):
                            startTime, endTime = return_value
                        else:
                            continue

                        newBlock = timeBlock(startTime, endTime, cohort.cohortName, currentCourse.courseName, 0, 0)
                        
                        # Store the first class found in the first iteration.
                        if day.classrooms[i].available_at_time(startTime, endTime):
                            if cohort.size <= day.classrooms[i].normalCapacity:
                                day.classrooms[i].timeBlocks.append(newBlock)
                                day.classrooms[i].currentBlockTime = endTime
                                break

    return copy.deepcopy(week)
"""
