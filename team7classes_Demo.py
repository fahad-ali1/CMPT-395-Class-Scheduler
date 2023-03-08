from team7classes import *

#-------------------------------------------------------------------------------
# USEFUL STUFF

sampleCohorts = [Cohort("A"), Cohort("B"), Cohort("C")]

def pause(text = "Press Enter..."):

    input(text)


#-------------------------------------------------------------------------------

def Demo_getClassroom():

    for classRoom in getClassrooms():

        classRoom.printClassroom()

def Demo_schedule():

    schedule = ScheduleLinkedList()

    schedule.addNodePush(3.0, sampleCohorts[0], 0, 0)
    schedule.addNodePush(0, sampleCohorts[1], 0, 0)
    schedule.addNodePush(0, sampleCohorts[2], 0, 0)

    print(schedule.getCohort(sampleCohorts[0]))

    return

if __name__ == '__main__':

    print("\nTesting Classes\n")

    # pause()
    # Demo_getClassroom()
    # pause()
    Demo_schedule()