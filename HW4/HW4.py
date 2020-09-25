###!/usr/bin/env python3
##"""
##Georgia Institute of Technology - CS1301
##HW4 - Lists - due Sept. 28, 2017
##"""
##__author__ = "Jared Raiola"
##__colab__ = """ I worked on the homework assignment alone, using only this semester's course materials. """
##"""
##Function name: remove_duplicates
##Parameters: aList
##Return value: the modified list
##Description:
##Write a function that takes in a list. Return a new list that has removed all of the
##duplicates from the first list. The modified list should have the unique elements in
##the same order as the original list. If there are no duplicates, then return the
##original list. If the original list is empty return an empty list.
##
##"""
##

def remove_duplicates(aList):
    newlist = [""]
    stored = []
    for num in range(len(aList)):
        for element in range(len(newlist)):
            if (aList[num] == newlist[element]):
                stored = []
                break
            stored = aList[num]
        if stored == []:
            continue
        newlist.append(stored)
    del(newlist[0])
    return newlist

##
##
##"""
##Function Name: common_elements
##Parameters: list1 and list2
##Return value: True if the two lists have at least one common element. False if they are different.
##Description:
##Write a function that takes in two lists. If the two lists have at least one common element,
##return True. If the two lists are completely different, return False. You can assume that
##none of the lists will be empty.
##
##"""
##

def common_elements(list1, list2):
    for i in list1:
        for q in list2:
            if i == q:
                return True
    return False

##
##
##"""
##Function Name: flatten_list
##Parameters: list1
##Return value: A list that contains the elements of the list passed in and the elements of the nested lists.
##Description:
##Write a function that takes a list and returns a new list. If any of the elements in the list
##are also lists, the returned list should have the individual elements of that nested list.
##You can assume that the nested list will not contain any elements that are also nested lists.
##If the original list is empty you can return an empty list.
##
##"""
##

def flatten_list(list1):
    newlist = []
    finallist = []
    for i in range(len(list1)):
        if type(list1[i]) == list:
            for entry in range(len(list1[i])):
                newlist.append(list1[i][entry])
        else:
            newlist.append(list1[i])
    return newlist
    

##
##
##"""
##Function Name: make_odd_even
##Parameters: list1
##Return Value: The modified list.
##Description:
##Write a function that takes a list and returns a new list. You can assume that the list passed
##in will only contain integers. If the elements of the list are even, add them to the new list.
##If the elements of the list are odd, make them even by adding 1 and then add that new number
##to the list. If the original list is empty you can return an empty list. You may assume the integer 0 is even.
##"""

def make_odd_even(list1):
    newlist = []
    for i in range(len(list1)):
        if (list1[i]%2==0):
            newlist.append(list1[i])
        else:
            newlist.append(list1[i]+1)
    return newlist

##
##
##"""
##Function Name: unique_lists
##Parameters: list1, list2
##Return value: The modified list1
##Description:
##Write a function that takes in two lists. If an element in list2 is not in list1, append that
##element to list1. If an element in list2 is already in list1, remove that element from list1.
##Return the updated list1.
##
##"""
##

def unique_lists(list1, list2):
    for i in range(len(list2)):
        count = 0
        for q in range(len(list1)):
            if list1[q] == list2[i]:
                del(list1[q])
                count = 0
                break
            else:
                count = 1
        if (count == 1):
            list1.append(list2[i])
    return list1

##
##
##"""
##Function name: process_string
##Parameters: aStr, aNum (int)
##Return value: a list of ints
##Description:
##Write a function that accepts a string of characters, filters out all non-number characters from the string,
##and returns a list of the numbers in the string that are a factor of aNum. NOTE: You can also ignore all zeroes
##(0) in the string, as 0 is not a factor of any number.
##
##"""
##
import string
def process_string(aStr, aNum):
    numlist = []
    intlist = []
    check = string.digits
    for i in range(len(aStr)):
        if aStr[i] in check:
            numlist.append(aStr[i])
    for q in range(len(numlist)):
        if (int(numlist[q]) == 0):
            continue
        elif (aNum % int(numlist[q]) == 0):
            intlist.append(int(numlist[q]))
    return intlist

##
##
##"""
##Function name: find_family
##Parameters: names_list (a list of strings); surname (string)
##Return value: a list containing the first names of all the people that have the parameter-specified surname
##AND do not have middle names.
##Description:
##Write a function that takes in a list of names and a specific surname to search for. Return a list of the
##first names of all the names in names_list that have surname AND do not have middle names. NOTE: Each name
##could have 0 or more middle names, but all names have a first and last name.
##"""
##

def find_family(names_list, surname):
    family = [""]
    stored = ""
    for i in range(len(names_list)):
        count = 0
        firstName = ""
        if surname in names_list[i]:
            stored = (names_list[i])
            for char in stored:
                if char == " ":
                    count += 1
                elif count == 0:
                    firstName += char
            if count > 1:
                continue
            else:
                check = False
                for q in range(len(family)):
                    if family[q] == firstName:
                        break
                    elif q == len(family)-1:
                        check = True
                if check == True:
                    family.append(firstName)
    del(family[0])
    return family
    
    
##
##"""
##Function name: add_next
##Parameters: aList (a list of integers)
##Return value: None
##Description: Overwrite each element in aList with its value added with the value of the next element in the list. The last element on the list (or if there is only one element in the list) should be added to itself.
##
##Note: Be aware that we are asking you to change the list in place, that is we are not asking you to return a new list with the modified changes, we want you to override the list we provide as an argument. Read this for more info and help:
##http://interactivepython.org/runestone/static/thinkcspy/Lists/UsingListsasParameters.html
##"""
##

def add_next(aList):
    for i in range(len(aList)):
        if i < (len(aList)-1):
            aList[i] = aList[i] + aList[i + 1]
        elif i == (len(aList) - 1):
            aList[i] = aList[i] + aList[i]
    

##
##"""
##Function name: election_day
##Parameters: a nested list; each list will contain three values; the first value will be the name of a
##candidate (str), the second value will be the total number of votes this candidate received (int) ,
##and the third parameter will be the two-letter abbreviation of a U.S. state (str).
##Return value: a string representation of the winning candidate, the total number of votes the
##candidate received, and the state in which the candidate received the most votes
##Description:
##You are helping total the votes for a nationwide political election. Write a function that returns a
##string with the name of the winning candidate (i.e. the candidate who received the highest total number
##of votes across all states), the total number of votes for that candidate, and the state in which the
##candidate received the most votes. If two candidates are tied for highest number of votes, your function
##should return information for the candidate that appears first in the list.
##Note: Failing to return the exact format of the string will cause you to lose points.
##(Format: Candidate name[comma][space] total # of votes [comma][space] two-letter state abbreviation)
##"""
##

def election_day(votes):
    sepNames = [""]
    voteList = []
    location = [""]
    stored = []
    test = 0
    votePos = 0
    highest = 0
    for num in range(len(votes)):
        for element in range(len(sepNames)):
            if (votes[num][0] == sepNames[element]):
                stored = []
                break
            stored = votes[num][0]
        if stored == []:
            continue
        sepNames.append(stored)
    del(sepNames[0])
    for name in range(len(sepNames)):
        voteList.append(0)
    for i in range(len(sepNames)):
        for q in range(len(votes)):
            if (sepNames[i] == votes[q][0]):
                voteList[i] += votes[q][1]
    for g in range(len(voteList)):
        if voteList[g] > highest:
            highest = voteList[g]
            votePos = g
    for v in range(len(votes)):
        if (votes[v][0] == sepNames[votePos]):
            if votes[v][1] > test:
                test = votes[v][1]
                location = votes[v][2]
    return "{}, {}, {}".format(sepNames[votePos], highest, location)









