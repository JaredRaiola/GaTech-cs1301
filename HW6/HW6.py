#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW4 - File I/O - due Oct. 12, 2017
"""
__author__ = "Jared Raiola"
__collaboration__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

"""
Function name: affordable_homes
Parameters: max_price (int), min_size (int), num_homes (int), outFile (string)
Return value: None
Description:  You will write to the file, outFile, a certain number
of homes, given by the parameter num_homes, that cost strictly less than the
max_price and are strictly greater than the min_size. If no homes meet the
qualifications then leave outFile empty. The homes that meet the qualifications
will be written to outFile in order from cheapest to most expensive in the
following format:
1. ADDRESS: [HOUSE ADDRESS]
	COST: $[HOUSE COST]
2. ADDRESS: [HOUSE ADDRESS]
	COST: $[HOUSE COST]
â€¦â€¦
"""

def affordable_homes(max_price, min_size, num_homes, out_file):
    inFile = open("data.csv", "r")
    aList = inFile.readlines()
    inFile.close()
    out = open(out_file, "w")
    count = 0
    newlist = []
    for i in range(1,len(aList)):
        line = aList[i]
        pieces = line.split(',')
        print(pieces)
        if int(pieces[6]) > min_size and int(pieces[9])<max_price:
            newlist.append(pieces)
    while count < num_homes:
        lowestprice = 0
        location = 0
        position = ""
        for num in range(len(newlist)):
            if num == 0:
                lowestprice = float(newlist[num][9])
                position = newlist[num][0]
                location = num
            elif float(newlist[num][9]) < lowestprice:
                lowestprice = float(newlist[num][9])
                position = newlist[num][0]
                location = num
            elif float(newlist[num][9]) == lowestprice and newlist[num][0] < position:
                lowestprice = float(newlist[num][9])
                position = newlist[num][0]
                location = num
        if newlist != []:
            count +=1
            out.write(str(count))
            out.write(". Address: ")
            out.write(position)
            out.write("\n")
            out.write("\tCost: $")
            out.write(str(lowestprice))
            out.write("\n")
        else:
            break
        if newlist != []:
            del newlist[location]
    out.close()
    


"""
Function name: home_profile
Parameters: address (string), redoFile (boolean)
Return value: None
Description: Write a profile of the home whose address (string) is passed into
the function to the file â€œprofileFile.txtâ€. Assume the address given is always
valid. If the boolean value redoFile is True, then start the file over (begin
at a blank file and write the house description to the initially empty file).
If redoFile is False, then simply append the description of the address passed
in to the bottom of the file. Write the address of the home to
â€˜profileFile.txtâ€™ in the following format:
Address:
[ADDRESS OF HOME PASSED IN]
[CITY], [STATE]
Rooms:
[NUMBER OF BEDROOMS] beds, [NUMBER OF BATHS], baths
"""

def home_profile(address, redo_file):
    inFile = open("data.csv", "r")
    aList = inFile.readlines()
    inFile.close()
    location = ""
    state = ""
    beds = ""
    baths = ""
    for i in range(1,len(aList)):
        line = aList[i]
        pieces = line.split(',')
        if address in pieces[0]:
            location = pieces[1]
            beds = pieces[4]
            baths = pieces[5]
            state = pieces[3]
    if redo_file == True:
        out = open("profileFile.txt","w")
    elif redo_file == False:
        aFile = open("profileFile.txt","r")
        stored = aFile.read()
        aFile.close()
        out = open("profileFile.txt", "w")
        out.write(stored)
    if location != "":
        out.write("Address:\n")
        out.write(address)
        out.write("\n")
        out.write(location)
        out.write(", ")
        out.write(state)
        out.write("\nRooms:\n")
        out.write(beds)
        out.write(" beds, ")
        out.write(baths)
        out.write(" baths\n\n")
    out.close()


"""
Function name: sold_day
Parameters: day (string)
Return value: int
Description: Write a function called sold_days that will take in a three letter
abbreviation of a day of the week. Count up how many houses were sold on that
day of the week. Return the number of houses sold on that day as an int. If an
invalid string is passed in as the day, return -1.

"""

def sold_day(day):
    inFile = open("data.csv", "r")
    aList = inFile.readlines()
    inFile.close()
    count = 0
    daylist = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if day not in daylist:
        return -1
    for i in range(1,len(aList)):
        line = aList[i]
        pieces = line.split(',')
        if day in pieces[8]:
            count += 1
    return count
            


"""
Function name: make_roster
Parameters: students (str), filename (str)
Return value:  None
Description: Take in a string of students. The format of the students will be
â€œFirst Last, First Last, First Lastâ€. Write the names of the students to the
file specified by the parameter. Write each line in the format â€œLast, Firstâ€.
Each student should be in a different line, and the students should be sorted
alphabetical by last name. Make sure there is no newline character after the
last student
"""

def make_roster(students, filename):
    sepstud = students.split(',')
    newlist = []
    lowest = ""
    for i in range(len(sepstud)):
        line = sepstud[i]
        piece = line.split(' ')
        if piece[0] == '':
            del piece[0]
        newlist.append(piece[0])
        newlist.append(piece[1])
    out = open(filename, "w")
    while newlist != []:
        position = 0
        for num in range(1, len(newlist), 2):
            if num == 1:
                lowest = newlist[num]
                position = num
            elif newlist[num] < lowest:
                lowest = newlist[num]
                position = num
        out.write(newlist[position])
        out.write(', ')
        out.write(newlist[position-1])
        del newlist[position-1]
        del newlist[position-1]
        if newlist != []:
            out.write('\n')
    out.close()
        

"""
Function name: choose_group
Parameters: aList(str), num (int), filename (str)
Return value:  Boolean (True or False)
Description: Write a function that takes in a list of student names. You will
form a group of size num from the group of names. You will choose the last num
students in the list. You will write out the names of the students who will
form the group to the filename passed in. This will be the format:
Team: [Name1], [Name2], [NameNum]
If there are not enough students for a group, write â€˜Not enough people for a
group.â€™ to the file. If there are zero people on a team then leave the file
empty. Finally, return True if there are enough people to form a group and
False otherwise.

"""

def choose_group(aList, num, filename):
    size = len(aList)
    out = open(filename, "w")
    if num <= size and num !=0:
        out.write("Team: ")
        for i in range(size-1,(size-1)-num, -1):
            out.write(aList[i])
            if i != size-num:
                out.write(", ")
        out.close()
        return True
    elif num > 0:
        out.write("Not enough people for a group.")
        out.close()
        return False
    elif num == 0:
        out.close()
        return False


"""
Function name: get_roster
Parameters: file_name (str)
Return value:  roster  (list)
Description: Read in a file whose the format shown above. Generate a list with
every studentâ€™s name. Make sure the names do not contain newline characters
(\n) and are in the order they appear in the file. Assume the passed in
filename is a valid file.
"""

def get_roster(file_name):
    inFile = open(file_name, "r")
    aList = inFile.readlines()
    inFile.close()
    namelist = []
    for i in range(len(aList)):
        line = aList[i].strip()
        if "Test" not in line and line != '':
            namelist.append(line)
    return namelist


"""
Function name: tests_missed
Parameters: file_name (str)
Return value: tests_missed (list)

Description: Read in a file whose the format shown above. For every DNT scores,\
add the test number to a list. Return the list at the end. The order of tests
should be the same order as the DNT scores are encountered. If multiple people
did not take the same test, the test number should be included in the list
multiple times. Assume the passed in filename is a valid file.
"""

def tests_missed(file_name):
    inFile = open(file_name, "r")
    aList = inFile.readlines()
    inFile.close()
    DNTlist = []
    for i in range(len(aList)):
        line = aList[i].strip()
        if "DNT" in line and line != '':
            stored = ""
            for char in line:
                if char in "0123456789":
                    stored += char
            DNTlist.append(int(stored))
    return DNTlist

"""
Function name: find_avg
Parameters: file_name (str), student_name (str)
Return value: student_avg (float)

Description: Read in a file whose the format shown above. Find the student
specified by the parameter. Generate the average of all the studentâ€™s score and
return the average. If the student has a DNT, disregard that score (do not use
that to compute the average). Round the answer to 2 decimal places. Assume not
two students have the same name and every student will have at least one valid
test. If the name of the student passed in is not in the file, return 0. Assume
the passed in filename is a valid file.
"""

def find_avg(file_name, student_name):
    inFile = open(file_name, "r")
    aList = inFile.readlines()
    inFile.close()
    curname = ""
    added = 0
    count = 0
    average = 0
    gradelist = []
    for i in range(len(aList)):
        line = aList[i].strip()
        if "Test" not in line and line != '':
            curname = line
        if curname == student_name:
            if "Test" in line and line != '':
                if "DNT" not in line and line != '':
                    stored = ""
                    piece = line.split(':')
                    for char in piece[1]:
                        if char in "0123456789" or char == '.':
                            stored += char
                    gradelist.append(float(stored))
    for num in range(len(gradelist)):
        added += gradelist[num]
        count += 1
    if count != 0:
        average = added/count
    return round(average, 2)







