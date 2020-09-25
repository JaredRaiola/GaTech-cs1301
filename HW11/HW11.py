"""
Georgia Institute of Technology - CS1301
HW11 - Recursion - due Monday, December 4, 2017
"""

__author__ = """Jared Raiola"""
__collaboration__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

"""
Function name: leaning_pyramid
Parameters: int
Returns: None
Description: Write a function that takes in a positive integer n (n â‰¥ 1). Use 
this integer to draw a leaning pyramid made out of stars (*). The base of the 
pyramid will consist of n stars, the next level of the pyramid will consist of 
n - 1 stars, etc. The top will be a single star. 
"""


def leaning_pyramid(num):
    if num == 0:
        pass
    else:
        leaning_pyramid(num-1)
        print('*'*num)


"""
Function name: reverse_phrase
Parameters: string
Returns: string
Description: Write a function that accepts one parameter, a string.  
Use recursion to reverse all the characters in the phrase. Keep in mind that 
you are reversing the entire string regardless of what it contains.
"""


def reverse_phrase(aStr):
    if len(aStr) == 0:
        return ""
    else:
        return reverse_phrase(aStr[1:]) + aStr[0]


"""
Function name: find_parenthesized_string
Parameters: string
Returns: string
Description: Given a string that contains a single pair of parenthesis, compute 
recursively a new string made up of only the parenthesis and the contents 
between them. Assume the single pair of parentheses will always be included in 
the string and that no other parenthesis will exist in the string. Return the 
computed string. You may not use .find in your solution.
"""


def find_parenthesized_string(aStr):
    if aStr[0] != "(":
        aStr = aStr[1:]
        return find_parenthesized_string(aStr)
    if aStr[len(aStr)-1] != ")":
        aStr = aStr[0:len(aStr)-1]
        return find_parenthesized_string(aStr)
    if aStr[0] == "(" and aStr[len(aStr)-1] == ")":
        return aStr

##Chop off elements from the front until you hit a ( and then chop off elements from the back )

"""
Function name: factorial_dictionary
Parameters: int
Returns: dict
Description:	Define a recursive function that accepts a positive integer
parameter n (n â‰¥ 1) and returns a dictionary. The dictionary should contain, as 
a key, every number from 1 to the number passed in. The corresponding value for 
each key should be the factorial of that number. You may not use looping in your 
solution. 

Hint: When trying to solve factorial_dictionary(n), you first need to 
recursively get factorial_dictionary(n â€“ 1). How would you get from 
factorial_dictionary(n â€“ 1) to factorial dictionary(n)? 
"""


def factorial_dictionary(num):
    if num == 1:
        return {1:1}
    else:
        mydict = factorial_dictionary(num-1)
        mydict[num] = num * factorial_dictionary(num-1)[num-1]
        return mydict


"""
Function name: pascal_triangle
Parameters: int
Returns: list of ints
Description: Write a function that takes in an integer parameter n (n â‰¥ 0) and 
returns a list of the elements of that row (the nth row) in the Pascal Triangle.

Hint: When trying to solve pascal_triangle(n), you first need to recursively get
pascal_triangle(n â€“ 1). How would you get from pascal_triangle(n â€“ 1) to 
pascal_triangle(n)? 
"""


def pascal_triangle(anInt):
    if anInt == 0:
        return [1]
    else:
        aList = pascal_triangle(anInt-1)
        newlist = [1]
        for i in range(len(aList)-1):
            newlist.append(aList[i]+aList[i+1])
        newlist.append(1)
        return newlist







