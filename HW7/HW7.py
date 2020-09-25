#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW7 - Dictionaries - due Monday, Mar. 13, 2017
"""
__author__ = "Jared Raiola"
__collaboration__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

"""
Function name: scheduler
Parameters: a dictionary containing membersâ€™ names as keys, and lists of months that member is available as values
Returns: the best month to schedule the meet-up (str)


Description: Youâ€™re the event manager of the National Association of Python Coders, and you want to coordinate a big meet-up for your organization. Write a function
called scheduler that takes in a dictionary with membersâ€™ names as keys and lists of months during which the member is available to attend a meet-up, and returns
whichever month has the most club members available. If there is more than one month with the highest number of available club members, return the month that occurs
earlier in the year. NOTE: The list of months for each club member will contain integers 1-12; you should return the corresponding month name as a string (â€œJanuaryâ€,
â€œFebruaryâ€, â€œMarchâ€, etc.) Hint: It may be useful to use a dictionary for this step.


"""

def scheduler(aDict):
    monthlist = []
    check = []
    here = []
    chosenmonth = 0
    count = 0
    month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    names = list(aDict.keys())
    for i in range(len(names)):
        delList = []
        check = aDict[names[i]]
        for q in check:
            if monthlist == []:
                monthlist = check
                here = check
                break
            if q in monthlist:
                here.append(q)
    for k in here:
        for j in here:
            if k == j:
                count  += 1
            if count > chosenmonth:
                chosenmonth = k
    if chosenmonth == 0:
        return month[1]
    return month[chosenmonth]
        
        


"""
Function name: buy_albums
Parameters: a dictionary named album_buy_dict {key is the name of an album (string): value is a the albumâ€™s artist (string)}, a dictionary named artist_price_dict
{key is name of an artist (string): value is the price per album of all that artistâ€™s albums (float)}

Returns: a dictionary {key is the name of an artist (string): value is how much was paid in total for all of the albums we bought that were theirs (float)}

Description: Write a function that takes in a dictionary in which every key is the name of an album, and every is a string of the name of the albumâ€™s artist, as well
as a dictionary in which every key is an artistâ€™s name, and every value is a float of the price per album for that artist for all their albums. The function should
return a dictionary in which every key is the name of an artist whose album(s) you bought, and the value is the total amount you paid for the album(s) of that
particular artist (i.e. price per that artistâ€™s albums * total number of albums bought). The dictionary should also have a key-value pair where the key is â€œtotalâ€
and the value is the grand total for all of the albums you bought.

Notes:
- You can assume spelling and punctuation of the artist names in album_buy_dict and artist_price_dict will be the same for the same artist.

- Each album included in album_buy_dict means we bought one of that album.

- You can assume that â€œtotalâ€ will never be a key in the original dictionary.
- If you print out your returned dictionary the order of the artists may be different from ours, whatâ€™s important is that each artist (key) is correctly matched to their price totals (value).


"""

def buy_albums(album_buy_dict, artist_price_dict):
    totaldict = {}
    totalprice = 0
    for i in album_buy_dict.keys():
            for q in artist_price_dict.keys():
                if album_buy_dict[i] == q:
                    if q not in totaldict:
                        totaldict[q] = artist_price_dict[q]
                    else:
                        totaldict[q] += artist_price_dict[q]
    for g in totaldict.keys():
        totalprice += totaldict[g]
    totaldict["total"] = totalprice
    return totaldict

"""
Function name: translator
Parameters: a filename (str), a string

Returns: a string

Description: Write a function that takes in a filename and a string, then uses the file to create a dictionary with English words as the keys and the corresponding words in another language
as the values. In the string passed in, replace every word that is a key in the dictionary with the value that the key maps to and return that new string. NOTE: You can assume the file passed
in will always be in the format specified in the test cases below, and that the string will be all lowercase.


"""

def translator(file, aStr):
    fileIn = open(file,"r")
    aList = fileIn.readlines()
    fileIn.close()
    aDict = {}
    for i in range(len(aList)):
        aList[i] = aList[i].strip()
    for q in range(len(aList)):
        keylist = aList[q].split(",")
        aDict[keylist[0]] = keylist[1].strip()
    for g in aDict.keys():
        if g in aStr:
            aStr = aStr.replace(g,aDict[g])
    return aStr


"""
Function name: average_rating
Parameters: a dictionary named movies_dict {keys are the names of movies (string): values are a list of integer ratings from zero to ten (list of ints)}

Returns: a dictionary {keys are names of movies (string): values are that showâ€™s average rating (float)}


Description: Write a function that takes in a dictionary and returns a dictionary. The function will take in a dictionary, movies_dict, where the key will be a string that represents the name
of some movie and the value will be a list of integers representing ratings on a ten-point scale for that movie. The function should take this dictionary and make a new dictionary where the keys
will be strings of the movie name and the values will be the average rating for that movie (rounded to 2 decimal points).

"""

def average_rating(movies_dict):
    finaldict = {}
    for i in movies_dict.keys():
        add = 0
        count  = 0
        for g in movies_dict[i]:
            add += g
            count += 1
        total = add/count
        finaldict[i] = round(total, 2)
    return finaldict

"""
Function name: sentence_stats
Parameters: a string
Returns: a dictionary {keys are strings: values are lists or numbers}

Description: Make a function called sentence_stats that takes in a sentence (str) as a parameter and returns a dictionary containing the information detailed below:

{"uppercase": number of uppercase letters in the string (int), "lowercase": number of lowercase letters in the string (int), "vowels": number of uppercase and lowercase vowels (AEIOU) in the
string (int), "consonants": number of uppercase and lowercase consonants (including Y) in the string (int), "numbers": number of numbers (0123456789) in the string (int), "special_chars":
number of special characters (i.e. non-letters and non-numbers, not including spaces) in the string (int), "word_count": number of words in the string (int), "most_common": most common character
in the string other than the space character (str)}
"""
import string
def sentence_stats(aStr):
    aDict = {"uppercase":0,"lowercase":0,"vowels":0,"consonants":0,"numbers":0,"special_chars":0,"word_count":0,"most_common":""}
    count = 0
    most = 0
    for i in aStr:
        if i in string.ascii_uppercase:
            aDict["uppercase"] += 1
        if i in string.ascii_lowercase:
            aDict["lowercase"] += 1
        if i in "aeiouAEIOU":
            aDict["vowels"] += 1
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            aDict["consonants"] += 1
        if i in string.digits:
            aDict["numbers"] += 1
        if i in string.punctuation:
            aDict["special_chars"] += 1
        aList = aStr.split()
        aDict["word_count"] = len(aList)
        if i not in string.whitespace:
            if count == 0:
                most = aStr.count(i)
                aDict["most_common"] = i
                count += 1
            elif aStr.count(i) > most:
                most = aStr.count(i)
                aDict["most_common"] = i
    return aDict

