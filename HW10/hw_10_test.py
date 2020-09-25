"""
Georgia Institute of Technology - CS1301
Basic unittest for student usage in HW10.py homework.
"""
import unittest
from HW10 import *

__author__  = "Nikita Bawa & Christine Feng"
__version__ = "0.1"
__email__   = "nbawa3@gatech.edu"
__date__    = "Fall 2017"

class LinkedInTest(unittest.TestCase):
    def setUp(self):
        self.user_1 = User("Nikita Bawa")
        self.user_2 = User("Christine Feng")
        self.user_3 = User("Daniel Barrundia", {"Java": []})
        self.user_4 = User("Nico Rodriguez")
        self.user_5 = User("Cory Brooks")
        self.user_6 = User("Erica Chia", {"Python": [], "JavaScript": []})
        self.user_7 = User("Rodrigo Mejia")
        self.user_8 = User("David Wang")
        self.user_9 = User("Caroline Kish")
        self.user_10 = User("Tiffany Xu")
        
        self.company_1 = Company('Facebook', ['Java', 'Python', 'C'])
        self.company_2 = Company('Twitter', ['Python'])
        self.company_3 = Company("Google", ["CSS", "Android", "Java"])
        self.company_4 = Company("Amazon", ["Machine Learning", "Front-End", "Data Structures"])
        self.company_5 = Company("Microsoft", ["Windows", "JavaScript"])
        
        self.linkedin = LinkedIn()
        # TODO add more test cases yourself

    ############
    #   User   #
    ############

    def test_a1_init_name(self):
        self.assertEqual(self.user_1.name, "Nikita Bawa",  msg = "A User should be initialized with a name.")

    def test_a2_init_name_2(self):
        self.assertEqual(self.user_3.name, "Daniel Barrundia",  msg = "A User should be initialized with a name.")

    def test_a3_default_skills(self):
        self.assertEqual(self.user_1.skills, None,  msg = "A User should be initialized with their skills dictionary as None, unless otherwise specified.")

    def test_a4_init_skills(self):
        self.assertEqual(self.user_3.skills, {"Java": []},  msg = "A User should be initialized with the specified skills dictionary passed in as a parameter.")

    def test_a5_default_company(self):
        self.assertEqual(self.user_2.company, None,  msg = "Users should be initialized with their company as None.")

    def test_a6_default_connections(self):
        self.assertEqual(self.user_2.connections, [],  msg = "Users should be initialized with an empty connections list.")

    def test_a7_add_skill(self):
        self.user_1.add_skill("Python")
        self.assertEqual(self.user_1.skills, {"Python": []}, msg = "A new skill should be added to a user's skill dictionary and begin with no endorsemets")     

    def test_a8_add_skill_2(self):
        self.user_3.add_skill("Java")
        self.assertEqual(self.user_3.skills, {"Java": []},  msg = "A skill should not be added if it already exists in the users skill dictionary.")
        
    def test_a9_repr(self):
        representation = self.user_3.__repr__()
        self.assertEqual(representation, "A User named Daniel Barrundia, unemployed, skilled in Java, with 0 connections", msg = "Each user object should have a standard string representation based on attributes") 

    def test_b1_endorse(self):
        self.user_2.endorse(self.user_5, "Android")
        self.assertEqual(self.user_5.skills, {"Android": [self.user_2]} ,  msg = "If a user endorses another user for a skill they do not already have, the skill should be added to their skills dictionary.")
        
    def test_b2_endorse_2(self):
        self.user_2.endorse(self.user_3, "Java")
        self.assertEqual(self.user_3.skills, {"Java": [self.user_2]} ,  msg = "A user should be added to the endorsers list in the skills dictionary when they endorse another user")
        
    def test_b3_endorse_3(self):
        self.user_2.endorse(self.user_3, "Java")
        self.user_4.endorse(self.user_3, "Java")
        self.assertEqual(self.user_3.skills, {"Java": [self.user_2, self.user_4]} ,  msg = "A user should be added to the endorsers list in the skills dictionary when they endorse another user")
    
    def test_b4_connect(self):
        self.user_4.connect(self.user_7)
        self.assertEqual(self.user_4.connections, [self.user_7], msg = "A user should be added to another users connections list when they connect with them")
        
    def test_b5_connect_2(self):
        self.user_4.connect(self.user_7)
        self.assertEqual(self.user_7.connections, [self.user_4], msg = "A user should be added to another users connections list when they connect with them")
        
    ################
    #    Company   # 
    ################   
    
    def test_b6_hire(self):
        self.company_1.hire(self.user_8)
        self.assertEqual(self.company_1.employees, [self.user_8], msg = "A user should be added to the companies employee list when hired")
        
    def test_b7_hire_2(self):
        self.company_1.hire(self.user_8)
        self.assertEqual(self.user_8.company, self.company_1, msg = "The users company attribute should change once they get hired")
        
    def test_b8_hire_3(self):
        self.company_1.hire(self.user_8)
        self.company_1.hire(self.user_9)
        self.assertEqual(self.company_1.employees, [self.user_8, self.user_9], msg = "A user should be added to the companies employee list when hired")
    
    def test_b9_fire(self):
        self.company_1.hire(self.user_8)
        self.company_1.hire(self.user_9)
        self.company_1.fire(self.user_8)
        self.assertEqual(self.company_1.employees, [self.user_9], msg = "A user should be removed from the companies employee list when fired")
        self.assertEqual(self.user_8.company, None, msg = "A user's company should become None again after they get fired")
    
    def test_c1_downsize(self):
        self.user_3.endorse(self.user_2, "CSS")
        self.user_5.endorse(self.user_2, "CSS")
        self.user_7.endorse(self.user_2, "Python")
        self.user_1.endorse(self.user_2, "Java")
        self.user_6.endorse(self.user_2, "Python")

        self.user_8.endorse(self.user_6, "JavaScript")
        self.user_9.endorse(self.user_6, "Python")
        self.user_1.endorse(self.user_6, "Python")
        self.user_2.endorse(self.user_6, "Python")

        self.user_8.endorse(self.user_7, "Machine Learning")
        self.user_9.endorse(self.user_7, "Java")
        self.user_1.endorse(self.user_7, "C")
        self.user_2.endorse(self.user_7, "Python")

        self.user_8.endorse(self.user_3, "Machine Learning")
        self.user_9.endorse(self.user_3, "Java")

        self.user_9.endorse(self.user_4, "C")

        self.company_2.hire(self.user_2)
        self.company_2.hire(self.user_6)
        self.company_2.hire(self.user_7)
        self.company_2.hire(self.user_3)
        self.company_2.hire(self.user_4)

        self.company_2.downsize(3)
        self.assertEqual(self.company_2.employees, [self.user_2, self.user_6, self.user_7], msg = "The company should fire the employees with the least endorsements until it reaches the target size.")
        self.assertEqual(self.user_3.company, None, msg = "The user's company should be None if they get fired")
        self.assertEqual(self.user_4.company, None, msg = "The user's company should be None if they get fired")

    def test_c2_downsize_2(self):
        self.user_3.endorse(self.user_2, "CSS")
        self.user_5.endorse(self.user_2, "CSS")
        self.user_7.endorse(self.user_2, "Python")
        self.user_1.endorse(self.user_2, "Java")
        self.user_6.endorse(self.user_2, "Python")

        self.user_8.endorse(self.user_6, "JavaScript")
        self.user_9.endorse(self.user_6, "Python")
        self.user_1.endorse(self.user_6, "Python")
        self.user_2.endorse(self.user_6, "Python")

        self.user_8.endorse(self.user_7, "Machine Learning")
        self.user_9.endorse(self.user_7, "Java")
        self.user_1.endorse(self.user_7, "C")
        self.user_2.endorse(self.user_7, "Python")

        self.user_8.endorse(self.user_3, "Machine Learning")
        self.user_9.endorse(self.user_3, "Java")

        self.user_9.endorse(self.user_4, "C")

        self.company_2.hire(self.user_2)
        self.company_2.hire(self.user_6)
        self.company_2.hire(self.user_7)
        self.company_2.hire(self.user_3)
        self.company_2.hire(self.user_4)

        before_downsize = self.company_2.employees

        self.company_2.downsize(7)
        self.assertEqual(self.company_2.employees, before_downsize, msg = "No employee should get fired if the target number is greater than the number of employees")

    ################
    #   LinkedIn   # 
    ################   

    def test_c3_add_to_network(self):
        self.linkedin.add_to_network([self.user_2, self.user_6, self.user_7, self.user_3, self.user_4])
        self.assertEqual(self.linkedin.users, [self.user_2, self.user_6, self.user_7, self.user_3, self.user_4] , msg = "Users should be added to the list of users in the network.")


    def test_c4_search(self):
        self.user_3.endorse(self.user_2, "CSS")
        self.user_5.endorse(self.user_2, "CSS")
        self.user_7.endorse(self.user_2, "Python")
        self.user_1.endorse(self.user_2, "Java")
        self.user_6.endorse(self.user_2, "Python")

        self.user_8.endorse(self.user_6, "JavaScript")
        self.user_9.endorse(self.user_6, "Python")
        self.user_1.endorse(self.user_6, "Python")
        self.user_2.endorse(self.user_6, "Python")

        self.user_8.endorse(self.user_7, "Machine Learning")
        self.user_9.endorse(self.user_7, "Java")
        self.user_1.endorse(self.user_7, "C")
        self.user_2.endorse(self.user_7, "Python")

        self.user_8.endorse(self.user_3, "Machine Learning")
        self.user_9.endorse(self.user_3, "Java")

        self.user_9.endorse(self.user_4, "C")

        self.linkedin.add_to_network([self.user_2, self.user_6, self.user_7, self.user_3, self.user_4])
        self.assertEqual(self.linkedin.search("Python", 2), [self.user_6] , msg = "The list of users returned should have the skill Python endorsed more than 2 times")


    def test_c5_search_2(self):
        self.user_3.endorse(self.user_2, "CSS")
        self.user_5.endorse(self.user_2, "CSS")
        self.user_7.endorse(self.user_2, "Python")
        self.user_1.endorse(self.user_2, "Java")
        self.user_6.endorse(self.user_2, "Python")

        self.user_8.endorse(self.user_6, "JavaScript")
        self.user_9.endorse(self.user_6, "Python")
        self.user_1.endorse(self.user_6, "Python")
        self.user_2.endorse(self.user_6, "Python")

        self.user_8.endorse(self.user_7, "Machine Learning")
        self.user_9.endorse(self.user_7, "Java")
        self.user_1.endorse(self.user_7, "C")
        self.user_2.endorse(self.user_7, "Python")

        self.user_8.endorse(self.user_3, "Machine Learning")
        self.user_9.endorse(self.user_3, "Java")

        self.user_9.endorse(self.user_4, "C")

        self.linkedin.add_to_network([self.user_2, self.user_6, self.user_7, self.user_3, self.user_4])
        self.assertEqual(self.linkedin.search("Java", 4), [] , msg = "An empty list should be returned if there are no users with the skill endorsed the specified number of times.")

    def test_c6_company_repr(self):
        representation = self.company_3.__repr__()
        self.assertEqual(representation, "A Company called Google with 0 employee(s)", msg = "Each Company object should have a standard string representation based on its attributes")
        
    def test_c7_company_repr(self):
        self.company_3.hire(self.user_8)
        representation = self.company_3.__repr__()
        self.assertEqual(representation, "A Company called Google with 1 employee(s)", msg = "Each Company object should have a standard string representation based on its attributes")
        
    def test_c8_user_repr(self):
        self.company_3.hire(self.user_8)
        representation = self.user_8.__repr__()
        self.assertEqual(representation, "A User named David Wang, employed by Google, with 0 connections", msg = "A User object's string representation should skip the skills phrase if the user has no skills in their skills dictionary attribute.")

    def test_c9_find_unemployed(self):
        self.company_1.hire(self.user_1)
        self.company_2.hire(self.user_2)
        self.company_3.hire(self.user_3)

        self.linkedin.add_to_network([self.user_1, self.user_2, self.user_3, self.user_4, self.user_5])
        self.assertEqual(self.linkedin.find_unemployed(), [self.user_4, self.user_5] , msg = "Only users whose company attribute is None should be returned.")

    def test_d1_find_unemployed_1(self):
        self.company_1.hire(self.user_1)
        self.company_2.hire(self.user_2)
        self.company_3.hire(self.user_3)

        self.linkedin.add_to_network([self.user_1, self.user_2, self.user_3])
        self.assertEqual(self.linkedin.find_unemployed(), [] , msg = "An empty list should be returned if there are no unemployed users")

    def test_d2_strengthen_network(self):
        self.user_1.connect(self.user_2)
        self.user_1.connect(self.user_3)
        self.user_1.connect(self.user_4)
        self.user_1.connect(self.user_5)
        self.user_1.connect(self.user_6)

        self.user_2.connect(self.user_4)

        self.user_3.connect(self.user_4)
        self.user_3.connect(self.user_5)
        self.user_3.connect(self.user_6)
        self.user_3.connect(self.user_7)
        self.user_3.connect(self.user_8)

        self.user_4.connect(self.user_5)

        self.linkedin.add_to_network([self.user_1, self.user_2, self.user_3, self.user_4, self.user_5, self.user_6, self.user_7, self.user_8])
        self.assertEqual(self.linkedin.strengthen_network(), 4, msg = "The number of users with less than 3 connections should be returned")
 
    def test_d3_get_employees(self):
        self.company_1.hire(self.user_1)
        self.company_1.hire(self.user_2)
        self.company_1.hire(self.user_3)
        self.company_2.hire(self.user_4)

        self.linkedin.add_to_network([self.user_1, self.user_2, self.user_3, self.user_4, self.user_5])
        self.assertEqual(self.linkedin.get_employees(self.company_1), [self.user_1, self.user_2, self.user_3] , msg = "Only users who work for the specified company should be returned.")

    def test_d4_recruit(self):
        self.user_3.endorse(self.user_2, "CSS")
        self.user_5.endorse(self.user_2, "CSS")
        self.user_7.endorse(self.user_2, "Python")
        self.user_1.endorse(self.user_2, "Java")
        self.user_6.endorse(self.user_2, "Python")

        self.user_8.endorse(self.user_6, "JavaScript")
        self.user_9.endorse(self.user_6, "Python")
        self.user_1.endorse(self.user_6, "Python")
        self.user_2.endorse(self.user_6, "Python")

        self.user_8.endorse(self.user_7, "Machine Learning")
        self.user_9.endorse(self.user_7, "Java")
        self.user_1.endorse(self.user_7, "C")
        self.user_2.endorse(self.user_7, "Python")

        self.user_8.endorse(self.user_3, "Machine Learning")
        self.user_9.endorse(self.user_3, "Java")

        self.user_9.endorse(self.user_4, "C")

        self.linkedin.add_to_network([self.user_1, self.user_2, self.user_6, self.user_7, self.user_3, self.user_4])

        self.assertEqual(self.company_3.recruit(self.linkedin), [self.user_2, self.user_7, self.user_3] , msg = "Only users from the network who have one of the company's preferred skills should be returned")
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LinkedInTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
