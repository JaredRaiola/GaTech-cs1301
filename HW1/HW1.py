
###!/usr/bin/env python3
##"""
##Georgia Institute of Technology - CS1301
##Introduction to Functions using Python.
##"""
##__author__ = """ Jared Raiola """
##__collab__ = """ I worked on the assignment alone and referred to https://docs.python.org/2/library/math.html in order to find out how to use the math module pi. """
##
##"""
##Function name (1): weight_on_mars
##Parameters: N/A
##Return value: N/A
##Description: Write a Python program which accepts your weight on earth
##and prints out your weight on mars.
##1.  Ask the user to input their weight on earth in pounds.
##2.  Your weight on mars is 0.38 of your weight on earth.
##For example, if you weight 100 pounds on earth, you would weigh 38 pounds on mars.
##3.  Print out the answer in the format:â€œAt a weight of 100 pounds on earth, you would weigh 38 pounds on Marsâ€.
##"""

def weight_on_mars():
    earth_weight = float(input("Please enter your Earth weight in pounds:\n"))
    mars_weight = earth_weight * .38
    print("At a weight of {} pounds on Earth, you would weigh {} pounds on Mars.\n".format(earth_weight,mars_weight))


##"""
##Function name (2): volume_of_cone
##Parameters: N/A
##Return value: volume of the cone
##Description:
##Write a function that takes the radius and height from the user and calculates the volume of a cone.
##1.  Get the length of the radius of the cone from the user.
##2.  Get the height of the cone from the user.
##3.  Calculate the volume of a cone with the radius length and height entered by the user using the following formula:
##Volume = (Ï€ * radius^2 * height)/3
##4.  Return the volume of the cone rounded to two decimal places.
##"""

def volume_of_cone():
    radius = float(input("Enter the radius of the cone:\n"))
    height = float(input("Enter the height of the cone:\n"))
    import math
    volume = (math.pi * (radius * radius) * height) / 3
    return round(volume,3)

    
##"""
##Function name (3): calculate_velocity
##Parameters: initial_position, final_position, time
##Return value: N/A
##Description: Write a function that finds the velocity using the initial position, final position, and time passed in the function.
##1.  Calculate the velocity using the following formula:
##velocity = (finalPosition â€“ initialPosition)/time
##2.  Print the velocity in the following format: â€œWith an final position of 100 meters, initial position of 0 meters, and a time of 80 seconds, the velocity is 12.5 m/s.â€
##
##"""

def calculate_velocity(initial_position, final_position, time):
    velocity = (final_position - initial_position)/time
    print("With a final position of {} meters, initial position of {} meters, and a time of {} seconds, the velocity is {} m/s.\n".format(final_position, initial_position, time, velocity))


##"""
##Function name (4): liquid_converter
##Parameters: N/A
##Return value: N/A
##Description: Write a user-interactive function to convert any number of fluid ounces to the equivalent number of gallons, quarts, pints, and gills.
##1.  Get the number of fluid ounces as an integer from the user.
##2.  Calculate the total number of gallons, quarts, pints, and gills represented by the original number of fluid ounces, using the following information:
##    a.  There are 128 fluid ounces in a gallon.
##    b.  There is 32 fluid ounces in a quart.
##    c.  There are 16 fluid ounces in a pint.
##    d.  There are 4 fluids ounces in a gill.
##3.  Print the calculated number of gallons, quarts, pints, and gills in the following format (assuming the user entered 6523): â€œ6523 fluid ounces is 50 gallon(s), 3 quart(s), 1 pint(s), and 2 gill(s)â€
##"""

def liquid_converter():
    floz = float(input("Please enter the number of fluid ounces:\n"))
    gallon = floz//128
    newfloz = floz%128
    quart = newfloz//32
    newfloz = newfloz%32
    pint = newfloz//16
    newfloz = newfloz%16
    gill = newfloz/4
    print("{} fluid ounces is {} gallon(s), {} quart(s), {} pint(s), and {} gill(s).\n".format(floz,gallon,quart,pint,gill))


##"""
##Function name (5): calorie_counter
##Parameters: N/A
##Return value: N/A
##Description:
##Write a function that takes the number of meals and number of miles to calculate a personâ€™s caloric intake in a day.
##1.  Get the number of meals a person ate from the user.
##2.  Get the number of miles a person ran.
##3.  Calculate a personâ€™s caloric intake using the following:
##    a.  The average calories gained per meal is 500 calories.
##    b.  A person that has done no exercise has burned about 1600 calories.
##    c.  The average calories burned per mile of running is 95 calories.
##4.  If a person gains the same or more calories than they burn then you should print a positive number. If a person burns more than they gain you should print a negative number.
##5.  Print the result in the following format: â€œAfter eating 5 meals and running 2 miles, a person gained 2500 calories and burned 1790 calories, leading to an intake of 710 calories.â€
##"""

def calorie_counter():
    meals = int(input("Please enter the number of meals the person ate:\n"))
    miles = float(input("Please enter the number of miles a person ran:\n"))
    calgained = meals * 500
    calburned = 1600 + (miles * 95)
    totalcal = calgained - calburned
    print("After eating {} meal(s) and running {} mile(s), a person gained {} calories and burned {} calories, leading to an intake of {} calories.\n".format(meals, miles, calgained, calburned, totalcal))


##"""
##Function name (6): paycheck_computation
##Parameters: pay_rate, hours_worked, tax_rate
##Return value: personâ€™s take home pay
##Description: A personâ€™s pay is determined by the hours they worked times the hourly rate. Unfortunately, a percentage of their pay is taken out as taxes.
##Using the parameters listed above, calculate and return the amount that a personâ€™s paycheck will be for after taxes have been taken out.
##1.  The first parameter, pay_rate, contains a personâ€™s hourly pay.
##2.  The second parameter, hours_worked, contains a personâ€™s number of hours worked.
##3.  The third parameter, tax_rate, gives the amount taken from taxes as a fraction between 0 and 1.
##4.  Calculate the personâ€™s take home pay, which is their paycheck total after taxes have been deducted.
##5.  Return the personâ€™s take home pay.
##"""

def paycheck_computation(pay_rate, hours_worked, tax_rate):
    total_paycheck = (hours_worked * pay_rate) - (hours_worked * pay_rate * tax_rate)
    return round(total_paycheck,2)

##"""
##Function name (7): main
##Parameters: N/A
##Return value: N/A
##Description:
##This function has been started for you. It serves as an introduction for conditional statements (learned later in the course). All you have to do is ask the user what function they will like to call and make the function call yourself.
##1.  Ask the user to input the number of the function [1-6]
##2.  Replace the pass statements with your function calls.
##"""

def main():
#TODO: finish this function (replace the pass with function calls)#

    ans = input("Please enter the number of the the function you'd like to call(1 for weight_on_mars, 2 for volume_of_cone, 3 for calculate_velocity, 4 for liquid_converter, 5 for calorie_counter, 6 for paycheck_computation):\n")
    ans = int(ans)
    if  ans == 1:
        weight_on_mars()
    elif ans == 2:
        print(volume_of_cone())
    elif ans == 3:
        initial_position = float(input("Please enter the initial position:\n"))
        final_position = float(input("Please enter the final position:\n"))
        time = float(input("Please enter the time it takes to get between positions:\n"))
        calculate_velocity(initial_position, final_position, time)
    elif ans == 4:
        liquid_converter()
    elif ans == 5:
        calorie_counter()
    elif ans == 6:
        pay_rate = float(input("Please enter the pay rate:\n"))
        hours_worked = float(input("Please enter the number of hours worked:\n"))
        tax_rate = float(input("Please enter the tax_rate:\n"))
        print("$", paycheck_computation(pay_rate, hours_worked, tax_rate))
    else:
        print("Invalid Function.")

main()
