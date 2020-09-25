###!/usr/bin/env python3
##"""
##Georgia Institute of Technology - CS1301
##Introduction to Functions using Python.
##"""
##__author__ = "Jared Raiola"
##__colab__ = """ I worked on the homework assignment alone, using only this semester's course materials. """
##
##
##"""
##Function name (1): rearrange_vowels
##Parameters: string to be iterated through (str)
##Return value: string starting with all of the vowels of the original string, and ending
##with all of the consonants of the original string (str)
##Description:
##Write a function that takes in a string and separates all of the vowels from the consonants,
##and creates a new string made from the separated portions. The ordering of the vowels and
##consonants should be the same order that they are present in the string. Capitalization should
##also be preserved. Any spaces present in the original string should be ignored and not added to
##the final output. You must use a for each loop in this function to receive full credit.
##
##"""
##

def rearrange_vowels(userstring):
    stringv = ""
    stringc = ""
    for letter in userstring:
        if letter in "aeiouAEIOU":
            stringv += letter
        elif letter in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            stringc += letter
    userstring = stringv + stringc
    return userstring

##
##
##"""
##Function name (2): censor
##Parameters: string to censor (str)
##Return value: censored string (str)
##Description:
##You are working at a childrenâ€™s television network, and your job is to censor any words that could potentially be inappropriate.
##In order to do this, you have to replace certain letters with symbols. You must use a for loop in this function to receive full credit.
##The rules for censorship or as follows:
##
##1.	â€œaâ€ or â€œAâ€ â†’ â€œ!â€
##2.	â€œuâ€ or â€œUâ€ â†’ â€œ*â€
##3.	â€œiâ€ or â€œIâ€ â†’ â€œ@â€
##4.	â€œeâ€ or â€œEâ€ â†’ â€œ#â€
##
##"""
##

def censor(userstring):
    censoredstr = ""
    for letter in userstring:
        if letter in "aA":
            censoredstr += "!"
        elif letter in "uU":
            censoredstr += "*"
        elif letter in "iI":
            censoredstr += "@"
        elif letter in "eE":
            censoredstr += "#"
        else:
            censoredstr += letter
    return censoredstr

##
##
##"""
##Function name (3): odd_and_even_multiples
##Parameters: lower bound of the range and number used to calculate multiples (int), upper-bound of a range (int)
##Return value: string displaying the number of odds and evens (str) (follow the format below exactly)
##Description:
##Your function should iterate through a range from the lower bound of the range to the given upper-bound. Count the number of odd and even numbers that are multiples of the first parameter. Ensure that the upper bound is actually included in the range for this function. Be sure to return the string in the exact format below.
##
##"""
##

def odd_and_even_multiples(lowb,upb):
    counteven = 0
    countodd = 0
    for number in range(lowb, upb + 1, abs(lowb)):
        if (number%2 == 0):
            counteven += 1
        else:
            countodd +=1
    return "{} even multiple(s) and {} odd multiple(s) from {}-{}".format(counteven, countodd, lowb, upb)

##
##
##"""
##Function name (4): most_common_character
##Parameters: a word or sentence (str), a string containing characters that will be counted (str)
##Return value: a string representing which character of the second parameter appears most frequently in the phrase string (str).
##Description:
##Write a function that receives two strings as parameters. The first parameter is a sentence,
##while the second string will contain any combination of characters (letters, numbers, special characters, etc.).
##Your code should find which of the given characters in the second parameter appears most frequently in the sentence string.
##Case should not be ignored, so for example, â€œAâ€ and â€œaâ€ should be considered two different characters.
##If no characters appear, an empty string should be returned.
##
##"""
##

def most_common_character(aSent, aStr):
    times = 0
    mostcommon = ""
    for letter in aStr:
        count = 0
        for char in aSent:
            if (char == letter):
                count += 1
                if (count>times):
                    times = count
                    mostcommon = letter
    return mostcommon

##
##
##"""
##Function name (5): sum_multiples
##Parameters: lower bound of the range and number used to calculate multiples (int), upper-bound of a range (int)
##Return value: sum of the multiples found in the given range (int)
##Description:
##Your function should iterate through a range from the lower bound of the range to the given upper-bound, and,
##using the first parameter (which is also used for the lower bound), calculate the sum of any multiples found in the range.
##Ensure that the upper bound is actually included in the range for this function.
##
##
##"""
##

def sum_multiples(nonzero, upperbound):
    total = 0
    for num in range(nonzero, upperbound + 1, 1):
        if (num % nonzero == 0):
            total = total + num
    return total
        

##
##
##"""
##Function name (6): remove_vowels
##Parameters: a word (str)
##Return value: original word without vowels (str)
##Description:
##Write a function that takes a string as a parameter, removes the vowels from the string (upper and lowercase).
##It should return one string, consisting of the same letters of the original string, but without the vowels.
##Must iterate through the string.
##
##
##"""
##

def remove_vowels(aWord):
    weirdword = ""
    for letter in aWord:
        if letter in "aeiouAEIOU":
            continue
        elif letter in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            weirdword += letter
    aWord = weirdword
    return aWord
    

##"""
##Function name: guess_dumplings
##Parameters: number of dumplings ate (int)
##Return value: number of guesses the user took (int)
##Description:
##Write a function that takes an integer value of the number of dumplings you ate, and asks the user to try to guess this number.
##When the user guesses the correct value, print a congratulatory statement and tell them how many guesses it took.
##If the user inputs â€œquitâ€ (exactly the string quit, donâ€™t worry about edge cases like â€˜QUITâ€™ or â€˜Quitâ€™), your code should end, and print the correct answer.
##The integer returned if the user quits should be -1. If the user has not guessed the correct answer within the 5th try, print that theyâ€™ve lost the game, and return 0. You must use a while-loop.
##"""
##

def guess_dumplings(dumAte):
    count = 0
    while count <5:
        guess = input("What is your guess?\n")
        count += 1
        if (guess == "quit"):
            print("The correct answer was {}.\n".format(dumAte))
            return -1
        elif (int(guess) == dumAte):
            print("Correct! It took you {} tries.\n".format(count))
            return count
        elif (count<5):
            print("Wrong answer, try again.\n")
    print("You lose. The correct answer was {}.\n".format(dumAte))
    return 0

##
##
##"""
##Function name (8): tie
##Parameters: a number 2-9 specifying half the max width of the tie (int)
##Return value: N/A
##Description:
##Write a function that takes in a number specifying half the width of the tie as a parameter
##and prints a tie of those specifications. Make sure the tie prints in the correct format
##as shown in the example. Do not hardcode this. You must use a for-loop.
##
##"""
##

def tie(usernumber):
    count = 0
    for num in range(usernumber, 0, -1):
        makestring = str(num)
        print(" " * count + makestring * (num * 2) + " " * count)
        count +=1
    count -=1
    for num in range(1, usernumber + 1, 1):
        makestring = str(num)
        print(" " * count + makestring * (num * 2) + " " * count)
        count -= 1
    count +=1
    for num in range(usernumber, 0, -1):
        makestring = str(num)
        print(" " * count + makestring * (num * 2) + " " * count)
        count +=1
        

##
##
##"""
##Function name (9): floor_division
##Parameters: original number (int), divisor (int)
##Return value: the maximum number of times the divisor can fully fit in original number (int)
##Description:
##Write a function that takes two integers. The first number will be divided by the second number.
##Count maximum number of times the divisor can fully fit into the original number.
##You are essentially coding the floor division operator.
##You cannot use the // (that would trivialize this assignment. You must use a loop.
##
##
##"""
##

def floor_division(orig, div):
    remainder = orig
    count = 0
    while remainder >= div:
        remainder -= div
        count += 1
    return count

##
##
##
##"""
##Function name (10): multi_table
##Parameters: number to make the multiplication table for (int)
##Return value: N/A
##Description:
##Write a function that takes in a number as a parameter and prints the multiplication table for that number.
##The table should be printed in an easy to read format. The first row and column should display
##the numbers from 1 â€“ number specified. Do not hard code this. You must use a for-loop.
##
##"""
##

def multi_table(usernum):
    count = 1
    for num in range(1,usernum+1):
        for num2 in range(1,usernum+1):
            num2prnt = num2 * count
            if (num2prnt < 10):
                print (num2prnt, end="     ")
            elif (num2prnt < 100):
                print(num2prnt, end="    ")
            elif (num2prnt <1000):
                print(num2prnt, end="   ")
            else:
                print(num2prnt, end="  ")
        count +=1
        print("\n")

##
