#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW5 - Modules/Tuples - due Oct. 5, 2017
"""
__author__ = "Jared Raiola"
__collaboration__ = """ I worked on the homework assignment alone, using this semester's course materials and https://wiki.python.org/moin/HowTo/Sorting to sort in the recruiting_profile function. """

import math
"""
Function name: complex_calculator
Parameters: a string, a list
Return value: An int, a float, or None

Description: Write a function that takes two arguments. The first argument will be a name (string). The second argument will be a list of numbers. The name will decide what function from the math module will be used. Refer to the table below to decide which name will correspond to which math function. If the name passed into the function is not one in the table, return None. The list of numbers contains the arguments to be used for the math function. However, some of these math functions take only 1 parameter and others take 2. Assume that if the math function needs one parameter, the list will be of length one, and if the math function needs two parameters the list will be of length two.
Notes:
    - Assume that if a math function is called, the numbers in the list will work for that math function. This is not a case sensitive function (i.e. "ceil" is the same as "CEIL", "Ceil", or "cEil", etc.), you must account for this.
    -Some math functions might give a long decimal number. Please round the numbers to 3 decimal points if needed. 
    - Look in the python library to see which functions take 1 parameter and which take 2. You may find that reading https://docs.python.org/3/library/math.html will be helpful.
"""
def complex_calculator(string, alist):
    stored = 0
    if(string.lower() == "ceil"):
        stored = math.ceil(alist[0])
        return stored
    elif(string.lower() == "fabs"):
        stored = math.fabs(alist[0])
        return stored
    elif(string.lower() == "gcd"):
        for i in range(0,len(alist),2):
            stored = math.gcd(alist[i],alist[i+1])
        return stored
    elif(string.lower() == "pow"):
        for i in range(0,len(alist),2):
            stored = math.pow(alist[i],alist[i+1])
        return stored
    elif(string.lower() == "sin"):
        stored = math.sin(alist[0])
        stored = round(stored,3)
        return stored


"""
Function name: help_recruit
Parameters:  A string
Return value: A tuple of length 3

Description: Write a function that takes in a string that holds the information of a recruit. You may assume that the string will always be formatted in this way: "NAME: SPORT, RANK". Return a tuple in the format (SPORT (string), RANK (int), NAME (string))
-Please note there is a space before SPORT. The tuple that is returned must not have any spaces within the strings.
"""
def help_recruit(string):
    count = 0
    sport = ""
    rank = ""
    name = ""
    for i in range(len(string)):
        count += 1
        if string[i] == ":":
            break
        else:
            name += string[i]
    count += 1
    for q in range(count, len(string)):
        count += 1
        if string[q] == ",":
            break
        else:
            sport += string[q]
    for g in range(count, len(string)):
        rank += string[g]
    mytup = (sport, int(rank), name,)
    return mytup
            


"""
Function name: recruiting_profile
Parameters:  A list of strings, sport_name
Return value: A list of tuples

Description: Write a function that takes in a list of strings. The list can be empty, in which case return an empty list. Each string contains information about a person. You may assume that the string will always be formatted in this way: "NAME: SPORT, RANK". Call the help_recruit function to convert each string to a tuple. Find all the tuples that have sport_name and add them to a list sorted by their rank. However, the tuples in this list should be formatted as (RANK(int), SPORT(string), NAME(string)). No one will have the same rank. Return the list.
Notes:
- If you have a function that returns a tuple of length three another way you can call the function and store the returned values is:
    a, b, c = myfunc()
- When sorting the tuples, you may use a built-in function. 
"""
def recruiting_profile(stringlist, sport_name):
    mylist = []
    for i in range(len(stringlist)):
        stored = help_recruit(stringlist[i])
        if stored[0] == sport_name:
            temptup = (stored[1], stored[0], stored[2],)
            mylist.append(temptup)
    mylist.sort(key = lambda temptup: temptup[0])      
    return mylist
            


"""
Function name: precious_pets
Parameters:  A string
Return value: A tuple of length 2

Description: Write a function that takes in a string containing information about multiple pets. You may assume that the string will always be formatted in this way: "Pet_Name, Pet_Excitement_Level + Pet_Name, Pet_Excitement_Level + etc.". Using the information given in the string, find the pet with the highest excitement level, and return the pet's name and the pet's excitement level in a tuple formatted as (Pet_Name, Pet_Excitement_Level).
"""
def precious_pets(aStr):
    count = 0
    check = 0
    doglist = []
    highest = ()
    while count < len(aStr):
        name = ""
        excite = ""
        for i in range(count,len(aStr)):
            count += 1
            if aStr[i] == ",":
                break
            else:
                name += aStr[i]
        count += 1
        for q in range(count,len(aStr)):
            count += 1
            if aStr[q] == " ":
                break
            else:
                excite += aStr[q]
        mytup = (name, int(excite))
        doglist.append(mytup)
        count += 2
    for g in range(len(doglist)):
        if check == 0:
            highest = doglist[g]
            check += 1
        elif check > 0:
            if highest[1] < doglist[g][1]:
                highest = doglist[g]
            elif highest[1] == doglist[g][1]:
                highest = doglist[g]
    return(highest)


"""
Function name: hungry_puppies
Parameters: A list of tuples, a float, a float
Return value: A tuple

Description: Write a function that takes a list of tuples, a float representing the price per a pound of food, and a float representing the total amount of money that can be spent on dog food. The tuples in the list contain a puppy's name (string), the puppy's age (int), and how many pounds of food the puppy can eat in a day (float). If the puppy is younger than 2, then only add half of the pounds that the puppy needs to eat. Return a tuple in the following order with the following information: (Boolean value representing if the amount of dog food can be afforded or not, Floating point value representing the total pounds of dog food that the puppies need, a String representing the name of the dog who needs the most food after taking into account the halving of the pounds).
Notes:
    - Assume all numbers in the tuples are positive. In the returned list, all numbers in the tuples should be floats.
    - The tuples can be in any order
    - If the list is empty, then return a tuple with True, 0, and an empty string
    - If there is a tie for which dog needs the most food, then add the dog who appears first to the tuple.
"""
def hungry_puppies(tupleList, price, dollars):
    totalfood = 0
    totalprice = 0
    mostfood = 0
    mostfoodname = ""
    for i in range(len(tupleList)):
        age = 0
        singlefood = 0
        halfsies = 0
        name = ""
        mytup = tupleList[i]
        for q in range(len(mytup)):
            if type(mytup[q]) == int:
                age = mytup[q]
            elif type(mytup[q]) == float:
                singlefood = mytup[q]
            elif type(mytup[q]) == str:
                name = mytup[q]
        if age < 2:
            totalfood += singlefood/2
            halfsies = singlefood/2
        else:
            totalfood += singlefood
        if halfsies > mostfood:
            mostfood = halfsies
            mostfoodname = name
        elif halfsies == 0 and singlefood > mostfood:
            mostfood = singlefood
            mostfoodname = name
    totalprice = totalfood * price
    if totalprice <= dollars:
        return (True, totalfood, mostfoodname,)
    else:
        return (False, totalfood, mostfoodname,)
            
                
                

"""
Function name: test_release
Parameters: a list of tuples
Return value: a list of tuples

Description: Write a function that takes in a list of tuples as a parameter and returns a tuple of each student's average in a list. Each tuple in the list will contain floating point values to represent exam grades and a string name. Return the average for each student in a tuple with the student's name first and the student's average second. Round the average to two decimal points. If there are less than three grades in the tuple, then do not include the student in the dictionary. If the list is empty, return an empty list.
"""
def test_release(tupList):
    finallist = []
    for i in range(len(tupList)):
        name = ""
        count = 0
        grades = 0
        average = 0
        thistup = ()
        mytup = tupList[i]
        for q in range(len(mytup)):
            if type(mytup[q]) == float or type(mytup[q]) == int:
                grades += mytup[q]
                count += 1
            if type(mytup[q]) == str:
                name = mytup[q]
        if count > 0:
            average = grades/count
            average = round(average, 2)
        else:
            continue
        if count < 3:
            continue
        else:
            thistup = (name, average,)
            finallist.append(thistup)
    return finallist








