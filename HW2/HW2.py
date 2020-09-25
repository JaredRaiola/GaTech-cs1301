#"""
##Georgia Institute of Technology - CS1301
##Introduction to Fruitful Functions and Conditionals using Python.
##"""
##__author__ = """Jared Raiola"""
##__collab__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

##"""
##
##""" PART 1: MARKET PLACE """
##
##"""
##Function name: is_in_stock
##Parameters: item (string), quantity (int)
##Return value: True or False (bool) or None (NoneType)
##Description:
##Write a function that determines whether or not the parameter item
##is in stock. If so, you also need to check that there are enough of
##that item in stock to fulfill your order (specified by the parameter
##quantity). Return True if these conditions are met, False
##otherwise. Return None if the item is not in the table.
##"""
##
 
def is_in_stock(item, quantity):
    if (item == "Avocado") or (item == "avocado"):
        return False
    elif (item == "Toothpaste") or (item == "toothpaste"):
        if (quantity > 0) and (quantity < 6):
            return True
        else:
            return False
    elif (item == "Popcorn") or (item == "popcorn"):
        if (quantity > 0) and (quantity < 11):
            return True
        else:
            return False
    elif (item == "Bottled Water") or (item == "Bottled water") or (item == "bottled water"):
        if (quantity > 0) and (quantity < 9):
            return True
        else:
            return False
    elif (item == "Phone Charger") or (item == "Phone charger") or (item == "phone charger"):
        if (quantity > 0) and (quantity < 2):
            return True
        else:
            return False
    else:
        return None
    
##
##"""
##Function name: can_afford
##Parameters: item (string), quantity (int), wallet (int)
##Return value: True or False (bool) or None (NoneType)
##Description:
##Write a function that determines whether or not you can afford the parameter
##item, given the number of that item you would like to buy (specified by
##parameter quantity), the amount of money you have (specified by parameter
##wallet), and the itemâ€™s current price value in the table. You do not need to
##consider whether there are enough of the item in stock for this function.
##Return True if you can afford this item, False otherwise. Return None
##if the item is not in the table.
##"""
##
    
def can_afford(item, quantity, wallet):
    if (item == "Avocado") or (item == "avocado"):
        if (quantity > 0) and (wallet >= 1 * quantity):
            return True
        else:
            return False
    elif (item == "Toothpaste") or (item == "toothpaste"):
        if (quantity > 0) and (wallet >= 2.75 * quantity):
            return True
        else:
            return False
    elif (item == "Popcorn") or (item == "popcorn"):
        if (quantity > 0) and (wallet >= 1 * quantity):
            return True
        else:
            return False
    elif (item == "Bottled Water") or (item == "Bottled water") or (item == "bottled water"):
        if (quantity > 0) and (wallet >= 4 * quantity):
            return True
        else:
            return False
    elif (item == "Phone Charger") or (item == "Phone charger") or (item == "phone charger"):
        if (quantity > 0) and (wallet >= 12 * quantity):
            return True
        else:
            return False
    else:
        return None
    
##
##"""
##Function name: is_on_sale
##Parameters: item (string)
##Return value: True or False (bool) or None (NoneType)
##Description:
##Write a function that determines whether or not the parameter item
##is on sale, according to the list price and current price values
##for the item in the table. You do not need to consider whether the item
##is in stock for this function. Return True if it is on sale, False otherwise.
##Return None if the item is not in the table.
##"""
##
    
def is_on_sale(item):
    if (item == "Avocado") or (item == "avocado"):
        curprice = 1
        if (curprice < 1.5):
            return True
        else:
            return False
    elif (item == "Toothpaste") or (item == "toothpaste"):
        curprice = 2.75
        if (curprice < 2.75):
            return True
        else:
            return False
    elif (item == "Popcorn") or (item == "popcorn"):
        curprice = 1
        if (curprice < 1):
            return True
        else:
            return False
    elif (item == "Bottled Water") or (item == "Bottled water") or (item == "bottled water"):
        curprice = 4
        if (curprice < 5.5):
            return True
        else:
            return False
    elif (item == "Phone Charger") or (item == "Phone charger") or (item == "phone charger"):
        curprice = 12
        if (curprice < 15):
            return True
        else:
            return False
    else:
        return None
    
##
##"""
##Function name: is_cheaper
##Parameters: item1 (string), item2 (string)
##Return value: 0, 1, or -1 (int) or None (NoneType)
##Description:
##Write a function that determines whether item1 is cheaperthan item2,
##based on their current prices. If item1 is cheaper than item2, return 1.
##You do not need to consider whether the items are in stock for this function.
##If item1 is more expensive than item2, return -1. If they are equally-priced,
##return 0. If either parameter item1 or item2 is invalid (i.e. is not included
##in the table), return None.
##"""
##
    
def is_cheaper(item1, item2):
    if (item1 == "Avocado") or (item1 == "avocado"):
        curprice1 = 1
        if(item2 == "Avocado") or (item2== "avocado"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Toothpaste") or (item2 == "toothpaste"):
            curprice2 = 2.75
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Popcorn") or (item2 == "popcorn"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Bottled Water") or (item2 == "Bottled water") or (item2 == "bottled water"):
            curprice2 = 4
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Phone Charger") or (item2 == "Phone charger") or (item2 == "phone charger"):
            curprice2 = 12
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        else:
            return None
    elif (item1 == "Toothpaste") or (item1 == "toothpaste"):
        curprice1 = 2.75
        if(item2 == "Avocado") or (item2== "avocado"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Toothpaste") or (item2 == "toothpaste"):
            curprice2 = 2.75
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Popcorn") or (item2 == "popcorn"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Bottled Water") or (item2 == "Bottled water") or (item2 == "bottled water"):
            curprice2 = 4
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Phone Charger") or (item2 == "Phone charger") or (item2 == "phone charger"):
            curprice2 = 12
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        else:
            return None
    elif (item1 == "Popcorn") or (item1 == "popcorn"):
        curprice1 = 1
        if(item2 == "Avocado") or (item2== "avocado"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Toothpaste") or (item2 == "toothpaste"):
            curprice2 = 2.75
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Popcorn") or (item2 == "popcorn"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Bottled Water") or (item2 == "Bottled water") or (item2 == "bottled water"):
            curprice2 = 4
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Phone Charger") or (item2 == "Phone charger") or (item2 == "phone charger"):
            curprice2 = 12
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        else:
            return None
    elif (item1 == "Bottled Water") or (item1 == "Bottled water") or (item1 == "bottled water"):
        curprice1 = 4
        if(item2 == "Avocado") or (item2== "avocado"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Toothpaste") or (item2 == "toothpaste"):
            curprice2 = 2.75
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Popcorn") or (item2 == "popcorn"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Bottled Water") or (item2 == "Bottled water") or (item2 == "bottled water"):
            curprice2 = 4
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Phone Charger") or (item2 == "Phone charger") or (item2 == "phone charger"):
            curprice2 = 12
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        else:
            return None
    elif (item1 == "Phone Charger") or (item1 == "Phone charger") or (item1 == "phone charger"):
        curprice1 = 12
        if(item2 == "Avocado") or (item2== "avocado"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Toothpaste") or (item2 == "toothpaste"):
            curprice2 = 2.75
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Popcorn") or (item2 == "popcorn"):
            curprice2 = 1
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Bottled Water") or (item2 == "Bottled water") or (item2 == "bottled water"):
            curprice2 = 4
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        elif (item2 == "Phone Charger") or (item2 == "Phone charger") or (item2 == "phone charger"):
            curprice2 = 12
            if (curprice1 == curprice2):
                return 0
            elif (curprice1 > curprice2):
                return -1
            else:
                return 1
        else:
            return None
    else:
        return None
    
##
##""" PART 2: CONCERT LISTING """
##
##"""
##Function name: is_single_cheaper
##Parameters: artistName (string)
##Return value: boolean
##Description:
##Write a function that takes in the name of one of the artists from the chart.
##Decide whether or not it would be cheaper to buy a single ticket, or to get the
##group ticket price and divide it amongst 10 people. If itâ€™s cheaper for single
##tickets, then return True, and if not, then return False. If the artist is not
##valid, return None.
##"""
##
    
def is_single_cheaper(artistName):
    if (artistName == "Taylor Swift"):
        return True
    elif (artistName == "Adele"):
        return False
    elif (artistName == "Zac Brown Band"):
        return False
    else:
        return None
    
##
##"""
##Function name: best_price
##Parameters: artistName (string)
##Return value: int representing the bevst price the user would pay to attend
##the artist's concert
##Description:
##Write a function that takes in the name of one of the artists from the chart.
##Using the is_single_cheaper function, determine whether a single ticket or group
##ticket would be the cheapest, and then return the price of the ticket as an integer.
##If the group option ends up being the cheapest, do not return the full price for the
##group, but the price once it is divided by 10 people. If the artist is not valid,
##return None.
##"""
##
    
def best_price(artistName):
    TorF = is_single_cheaper(artistName)
    if (artistName == "Taylor Swift"):
        if (TorF == True):
            price = 275
            return price
        elif (TorF == False):
            price = 3000/10
            return price
        else:
            return None
    elif (artistName == "Adele"):
        if (TorF == True):
            price = 152
            return price
        elif (TorF == False):
            price = 1500/10
            return price
        else:
            return None
    elif (artistName == "Zac Brown Band"):
        if (TorF == True):
            price = 25
            return price
        elif (TorF == False):
            price = 200/10
            return price
        else:
            return None
    else:
        return None

##
##
##"""
##Function name: all_three
##Parameters: None
##Return value: int representing how much it would cost to attend all three concerts
##Description:
##Write a function that uses the best_price function to determine the best prices of
##each of the concerts, sums them all up, and returns the total cost.
##"""
##
    
def all_three():
    price1 = best_price("Taylor Swift")
    price2 = best_price("Adele")
    price3 = best_price("Zac Brown Band")
    totalcost = price1 + price2 + price3
    return totalcost

##
##"""
##Function name: cheapest_concert
##Parameters: None
##Return value: string representing the name of the artist with the cheapest concert
##Description:
##Write a function that uses the best_price function to determine the best prices of
##each of the concerts, and then returns the name of the artist with the cheapest concert.
##You may not use any built in Python functions.
##"""
##

def cheapest_concert():
    price1 = best_price("Taylor Swift")
    price2 = best_price("Adele")
    price3 = best_price("Zac Brown Band")
    if (price1 < price2) and (price1 < price3):
        return ("Taylor Swift")
    elif (price2 < price1) and (price2 < price3):
        return ("Adele")
    else:
        return ("Zac Brown Band")

##
##"""
##Function name: add_two
##Parameters: artist1 (string), artist2 (string)
##Return value: int representing the cost to go to both concerts
##Description:
##Write a function that takes in two artists from the table above, and calculates how much
##it would cost to attend both concerts based on their best prices. Return the total cost.
##"""
##
    
def add_two(artist1, artist2):
    if (artist1 == "Taylor Swift") or (artist1 == "Adele") or (artist1 == "Zac Brown Band"):
        p1 = best_price(artist1)
        if (artist2 == "Taylor Swift") or (artist2 == "Adele") or (artist2 == "Zac Brown Band"):
            p2 = best_price(artist2)
            tc = p1 + p2
            return tc
        else:
            return None
    else:
        return None
    
##
##"""
##Function name: can_afford_concerts
##Parameters: money (int)
##Return value: None
##Description:
##Write a function that will be using some of the functions that you have written above. Based
##on the money passed in, determine if you can go to all three concerts, only two concerts, or
##only the cheapest concert. If you can go to all three, print â€œI can go to all three!â€, if you
##can only go to two of any combination, (Taylor Swift and Adele, Adele and Zac Brown Band, etc),
##then print â€œI can only go to two!â€, and if you can only go to one concert, print a statement
##in the format of â€œI can only go to one.â€. If there is not enough money for any of those options,
##then print out a statement that says â€œDang it, I canâ€™t go to any concert.â€.
##NOTE: Itâ€™s very important that you print out your answer EXACTLY as itâ€™s formatted in the instructions.
##"""
##
    
def can_afford_concerts(money):
    topcost = all_three()
    if (money >= topcost):
        print("I can go to all three!")
    else:
        twocost1 = add_two("Taylor Swift", "Adele")
        twocost2 = add_two("Taylor Swift", "Zac Brown Band")
        twocost3 = add_two("Adele", "Zac Brown Band")
        if (money >= twocost1) or (money >= twocost2) or (money >= twocost3):
            print("I can only go to two!")
        else:
            singlecost1 = best_price("Taylor Swift")
            singlecost2 = best_price("Adele")
            singlecost3 = best_price("Zac Brown Band")
            if (money >= singlecost1) or (money >= singlecost2) or (money >= singlecost3):
                print("I can only go to one.")
            else:
                print("Dang it, I can't go to any concert.")
                
##
##""" PART 3: MISCELLANEOUS """
##
##"""
##Function name: what_can_you_do
##Parameters: age (int)
##Return value: None
##Description:
##Write a function that takes in the age of the user and prints out all the activities they are able
##to do based on the table in the PDF. If they canâ€™t do any of those activities, print out â€œSorry, youâ€™re
##not old enough for any of theseâ€.
##"""
##
                
def what_can_you_do(age):
    if (age >= 65):
        print("You can vote, party, and retire.")
    elif(age>=21):
        print("You can vote and party")
    elif(age>=18):
        print("You can vote.")
    elif(age>=0):
        print("Sorry, you're not old enough for any of these.")
    else:
        print("Whoa there, that age is invalid. If you're a wizard, why didn't I get my acceptance letter to Hogwarts yet?")
    
##
##"""
##Function name: pass_or_fail
##Parameters: current_grade (int), final_weight (float), final_score (int)
##Return value: final letter grade A, B, C, D, or F (string)
##Description:
##Write a function that will take your current grade in a class, the weight of the final exam as a
##decimal between 0 and 1, and the score you got on the final exam to determine what letter grade
##you'll receive using the following formula:
##final_grade = current_grade * (1 - final_weight) + final_score * final_weight
##Use the following ranges for letter grades:
##A: 90-100
##B: 80-89.9999
##C: 70-79.9999
##D: 60-69.9999
##F: 0-59.9999
##"""
##
        
def pass_or_fail(current_grade, final_weight, final_score):
    final_grade = current_grade * (1 - final_weight) + final_score * final_weight
    if (final_grade >= 90):
        return "A"
    elif (final_grade >= 80) and (final_grade < 90):
        return "B"
    elif (final_grade >= 70) and (final_grade < 80):
        return "C"
    elif (final_grade >= 60) and (final_grade < 70):
        return "D"
    else:
        return "F"


