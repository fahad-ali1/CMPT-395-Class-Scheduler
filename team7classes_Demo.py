from team7classes import *

def Demo_getClassroom():

    for classRoom in getClassrooms():

        classRoom.printClassroom()

if __name__ == '__main__':

    print("\nTesting Classes\n")

    Demo_getClassroom()