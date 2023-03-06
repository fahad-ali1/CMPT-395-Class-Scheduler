'''
Author: Fahad Ali, Schuyler Kelly
Description: This program will create cohorts of the best size depending on
the class space available, and suggest (if required) more class space
'''

import math, itertools

class Classroom:

    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.current_students = cap
        self.in_use = False

    def __repr__(self):
        return f"'Name: {self.name}, Cap: {self.cap}, Current: {self.current_students}, Used: {self.in_use}'"


class Students:
    '''
    Description: this class will input students for each program and create
    appropriate cohorts. It will be implemented into the GUI app.
    '''
    def __init__(self):
        # initialize attributes
        self._BCOMStudents = 0
        self._PCOMStudents = 0

        self._PMStudents = 0
        self._BAStudents = 0
        self._SCMTStudents = 0
        self._FSStudents = 0
        self._DXDStudents = 0
        self._BKStudents = 0

        self._term = 0

        self._rooms = []
        with open("data/classrooms.csv", "r") as file:
            # Read each line into a list with no newline character
            rooms_data = [l.strip() for l in file if "sep=" not in l]
            for room in rooms_data:
                name, cap = room.split(",")[0], int(room.split(",")[1])
                self._rooms.append(Classroom(name, cap))

        # sort rooms by largest to smallest
        self._rooms = sorted(self._rooms, key=lambda x:x.cap, reverse=True)

    def cohorts_final(self):
        '''
        Description: this function will call divide_to_cohorts() and append
        the results to a list
        Returns: a list of lists of all the cohorts
        '''
        cohortList = []
        cohortList.append(self.divide_to_cohorts(self._PCOMStudents, "PC"))
        cohortList.append(self.divide_to_cohorts(self._BCOMStudents, "BC"))

        self._reset_classrooms(self._rooms)

        
        cohortList.append(self.divide_to_cohorts(self._PMStudents, "PM"))
        cohortList.append(self.divide_to_cohorts(self._BAStudents, "BA"))
        cohortList.append(self.divide_to_cohorts(self._SCMTStudents, "SCMT"))
        cohortList.append(self.divide_to_cohorts(self._BKStudents, "BK"))
        cohortList.append(self.divide_to_cohorts(self._FSStudents, "FS"))
        cohortList.append(self.divide_to_cohorts(self._DXDStudents, "DXD"))

        return cohortList
    
    def _reset_classrooms(self, classroom_list):
        for room in classroom_list:
            room.current_students = room.cap
            room.in_use = False
    
    def _check_room_combo(self, temp, combo, percent, wiggle_percent):

        # Iterate through each room in the combo
        for room in combo:
            wiggle_room = math.floor(room.cap - (room.cap * wiggle_percent))
            allowed_total = math.floor(room.cap - (room.cap * percent))

            # If the remaining students is less than the allowed total, return, as
            # this combination simply will not work.
            if temp - wiggle_room < 0:
                return None
            
            # Handle if the remaining students can reasonably fit into the room.
            if temp - wiggle_room >= 0:
                
                # Check conditions for if this room combo is acceptable.
                if room == combo[-1] and wiggle_room <= temp <= room.cap:
                    room.current_students = temp
                    return combo

                # Convert to int, as allowed total will be a float with ?.0 in it
                room.current_students = int(allowed_total)
                temp -= allowed_total
                if temp == 0:
                    return combo

    def most_even_rooms(self, students):

        empty_classrooms = []
        for room in self._rooms:
            if not room.in_use:
                empty_classrooms.append(room)

        if not empty_classrooms:
            return f"Need room for {students} students"
        
        percent = 0.05
        wiggle_room = 0.05
        result_found = False
        being_compared = 1
        while not result_found:
            for combo in itertools.combinations(empty_classrooms, being_compared):
                combo = list(combo)
                temp = students

                # Reset classrooms so that the state of classrooms is
                # identical for each check.
                # NOTE: I really don't know if this is necessary, it just
                #       eliminates the possibility of bugs.
                self._reset_classrooms(combo)
                combo_result = self._check_room_combo(temp, combo, percent, wiggle_room)

                if combo_result:
                    # Make the result mutable
                    combo_result = list(combo_result)

                    for result in combo_result:
                        result.in_use = True
                    return combo_result
                
            being_compared += 1
            
            # If being compared is 5, increase percent and reset combo value
            if being_compared == len(empty_classrooms) + 1:

                # Set conditions as a series of gates

                # If the percent is zero, start adjusting the wiggle room
                # that the final classroom can fit within
                if percent == 0:
                    if wiggle_room < 1:
                        wiggle_room += 0.01
                    else:
                        wiggle_room = 1

                # If the percentage isn't zero, reduce how much room should
                # remain in the classrooms
                if percent != 0:
                    percent -= 0.01
                    if percent < 0:
                        percent = 0
                
                being_compared = 1
        

    def divide_to_cohorts(self, students, program):
        '''
        Description: this function will assign the appropriate prefix and
        divide by cohort size and return a list
        Returns: a list of cohort strings
        '''

        cohorts = []
        # Example entry: "PM0101: 11-533, 38/40

        num = 1

        # If there are no students, return the cohorts, as no cohorts can
        # be created.
        if students == 0:
            return cohorts
        

        rooms = self.most_even_rooms(students)

        if type(rooms) == str:
            print(f"{rooms} in {program}")
            quit()

        if rooms:
            for room in rooms:
                string = f"{program}{self._term:02d}{num:02d}: {room.name}, {room.current_students}/{room.cap}"
                cohorts.append(string)
                num += 1
            
        return cohorts

if __name__ == "__main__":
    students = Students()
    students._PCOMStudents = 210
    students._BCOMStudents = 25
    students._BAStudents = 74
    students._PMStudents = 102
    students._SCMTStudents = 41
    students._FSStudents = 18
    students._DXDStudents = 0
    students._BKStudents = 0
    students._term = 1

    
    cohorts = students.cohorts_final()
    for cohort in cohorts:
        print(cohort)
