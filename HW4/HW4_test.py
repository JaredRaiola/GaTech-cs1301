import sys
import unittest
from unittest.mock import patch
import os
import importlib
"""
STUDENT autograder for HW04 - CS1301
"""

__author__ = "Christine Feng and Soni Aggarwal"
__version__ = "1.1"
__email__ = "christinefeng@gatech.edu, soni@gatech.edu"

class TestMyClass(unittest.TestCase):

    def test_remove_duplicates_1(self):
        errormsg = 'Failed remove_duplicates with ([10, "cat", 5.2, "hello", "cat", "Hello", 0]'
        self.assertEqual([10, 'cat', 5.2, 'hello', 'Hello', 0],
                         hw.remove_duplicates([10, "cat", 5.2, "hello", "cat", "Hello", 0]),
                         msg = errormsg)

    def test_remove_duplicates_2(self):
        errormsg = 'Failed remove_duplicates with [10, 35, 35, 10, 98, "hi", 35, "hi", 0, 0]'
        self.assertEqual([10, 35, 98, 'hi', 0],
                         hw.remove_duplicates([10, 35, 35, 10, 98, "hi", 35, "hi", 0, 0]),
                         msg = errormsg)

    def test_remove_duplicates_3(self):
        errormsg = 'Failed remove_duplicates with ["hi","hi","hi","hi","hi"]'
        self.assertEqual(['hi'],
                         hw.remove_duplicates(["hi","hi","hi","hi","hi"]),
                         msg = errormsg)

    def test_common_elements_1(self):
        errormsg = "Failed common_elements w/ [1, 2, 3, 4] and [6, 7, 8, 9, 10]"
        self.assertFalse(hw.common_elements([1, 2, 3, 4], [6, 7, 8, 9, 10]),
                         msg = errormsg)

    def test_common_elements_2(self):
        errormsg = 'Failed remove_duplicates with ["goodbye", 88, True, "yellow"] and ["orange", False, "red", "goodbye", 0]'
        self.assertTrue(hw.common_elements(["goodbye", 88, True, "yellow"], ["orange", False, "red", "goodbye", 0]),
                        msg = errormsg)

    def test_common_elements_3(self):
        errormsg = 'Failed common_elements with [] and []'
        self.assertFalse(hw.common_elements([],[]),
                         msg = errormsg)

    def test_flatten_list_1(self):
        errormsg = 'Failed flatten_list with [8, 9, [0, True, "ok"], False]'
        self.assertEqual([8, 9, 0, True, 'ok', False],
                         hw.flatten_list([8, 9, [0, True, "ok"],False]),
                         msg = errormsg)

    def test_flatten_list_2(self):
        errormsg = 'Failed flatten_list with ["hi", [5, "ok"], 8, "purple", [7, "bye", False], True]'
        self.assertEqual(['hi', 5, 'ok', 8, 'purple', 7, 'bye', False, True],
                         hw.flatten_list(["hi", [5, "ok"], 8, "purple", [7, "bye", False], True]),
                         msg = errormsg)

    def test_flatten_list_3(self):
        errormsg = """Failed flatten_list w/ ["no", "sub", "lists", "in", "this", "one"]."""
        self.assertEqual(['no', 'sub', 'lists', 'in', 'this', 'one'],
                         hw.flatten_list(["no", "sub", "lists", "in", "this", "one"]),
                         msg = errormsg)

    def test_flatten_list_4(self):
        errormsg =  """Failed flatten_list w/ [[1, 2], [3, 4], [5, 6]]."""
        self.assertEqual([1, 2, 3, 4, 5, 6],
                         hw.flatten_list([[1, 2], [3, 4], [5, 6]]),
                         msg = errormsg)

    def test_flatten_list_5(self):
        errormsg =  """Failed flatten_list w/ [False, "dress", ["wall"], 234, ["7", "seven"]]."""
        self.assertEqual([False, 'dress', 'wall', 234, '7', 'seven'],
                         hw.flatten_list([False, "dress", ["wall"], 234, ["7", "seven"]]),
                         msg = errormsg)

    def test_make_odd_even_1(self):
        errormsg = "Failed make_odd_even with [2, 43, 23, 34, 20, 88, 7]"
        self.assertEqual([2, 44, 24, 34, 20, 88, 8],
                         hw.make_odd_even([2, 43, 23, 34, 20, 88, 7]),
                         msg = errormsg)

    def test_make_odd_even_2(self):
        errormsg = "Failed make_odd_even with [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
        self.assertEqual([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10],
                         hw.make_odd_even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         msg = errormsg)

    def test_make_odd_even_3(self):
        errormsg =  """Failed make_odd_even w/ []."""
        self.assertEqual([], hw.make_odd_even([]), msg = errormsg)

    def test_make_odd_even_4(self):
        errormsg = """Failed make_odd_even w/ [1, 3, 5, 7, 9]."""
        self.assertEqual([2, 4, 6, 8, 10],
                         hw.make_odd_even([1, 3, 5, 7, 9]), msg = errormsg)

    def test_make_odd_even_5(self):
        errormsg = """Failed make_odd_even w/ [2, 4, 6, 8, 10]."""
        self.assertEqual([2, 4, 6, 8, 10],
                         hw.make_odd_even([2, 4, 6, 8, 10]), msg = errormsg)

    def test_unique_lists_1(self):
        errormsg = "Failed unique_lists with [6, 'butterfly', 'waffle', 19] and [True, 'shirt', 8, 'waffle', 6, 'computer']"
        self.assertEqual(['butterfly', 19, True, 'shirt', 8, 'computer'],
                         hw.unique_lists([6, "butterfly", "waffle", 19], [True, "shirt", 8, "waffle", 6, "computer"]),
                         msg = errormsg)

    def test_unique_lists_2(self):
        errormsg = "Failed unique_lists with ['water', 'sand', 'beach', 14] and [False, 'earring', 'smile', 17]"
        self.assertEqual(['water', 'sand', 'beach', 14, False, 'earring', 'smile', 17],
                         hw.unique_lists(["water", "sand", "beach", 14],[False, "earring", "smile", 17]),
                         msg = errormsg)

    def test_unique_lists_3(self):
        errormsg = """Failed unique_lists w/ [False, True, "hi", "teal", "toothfairy"] and [False, True, "hi", "teal", "toothfairy"]."""

        self.assertEqual([],
                         hw.unique_lists([False, True, "hi", "teal", "toothfairy"], [False, True, "hi", "teal", "toothfairy"]),
                         msg = errormsg)

    def test_unique_lists_4(self):
        errormsg = """Failed unique_lists w/ [] and []."""
        self.assertEqual([], hw.unique_lists([], []), msg = errormsg)


    def test_unique_lists_5(self):
        errormsg = """Failed unique_lists w/ [1, 2, [1, 2], 3, [4, [5]]] and [1, 2, 3, 4, 5]."""
        self.assertEqual([[1, 2], [4, [5]], 4, 5],
                         hw.unique_lists([1, 2, [1, 2], 3, [4, [5]]], [1, 2, 3, 4, 5]),
                         msg = errormsg)

    def test_process_string_1(self):
        errormsg = "Failed process_string with 'jahfig234thdajg0gri9t2832488radga' and 12."
        self.assertEqual([2, 3, 4, 2, 3, 2, 4],
                         hw.process_string("jahfig234thdajg0gri9t2832488radga", 12),
                         msg = errormsg)

    def test_process_string_2(self):
        errormsg = 'Failed process_string with "aoweh102935jgalhfda03191jfwl" and 7.'
        self.assertEqual([1, 1, 1],
                         hw.process_string("aoweh102935jgalhfda03191jfwl", 7),
                         msg = errormsg)

    def test_process_string_3(self):
        errormsg = 'Failed process_string with "!@#^%&*&$%@$^^$%$#%^&*(){}|<><,.,??./ and 31.'
        self.assertEqual([], hw.process_string("!@#^%&*&$%@$^^$%$#%^&*(){}|<><,.,??./", 31),
                         msg = errormsg)

    def test_find_family_1(self):
        errormsg = 'Failed find_family test case 1. See out.txt for test case.'
        names_1 = ["Josh Washington", "Chris Hartley", "Sam Giddings", "Beth Washington", "Jessica Riley", "Ashley Brown", "Hannah Washington", "Mike Munroe", "Matt Taylor", "Emily Davis"]
        self.assertEqual(['Josh', 'Beth', 'Hannah'],
                         hw.find_family(names_1, "Washington"),msg = errormsg)

    def test_find_family_2(self):
        errormsg = 'Failed test_find_family_2'
        names_2 = ["Esteban Julio Ricardo Montoya de la Rosa Ramirez", "Lina Ramirez", "Sebastian Alejandro Ramirez", "Zack Martin", "Cody Martin", "Jonathan Romero", "Daniela Ramirez"]
        self.assertEqual(['Lina', 'Daniela'],
                         hw.find_family(names_2, "Ramirez"), msg = errormsg)

    def test_find_family_3(self):
        errormsg = 'Failed test_find_family_3'
        names_3 = ["John Smith", "John Smith", "Jane Smith", "Jane Doe Smith", "John Smith", "Jane Smith", "John Doe Smith"]
        self.assertEqual(['John', 'Jane'],
                         hw.find_family(names_3, "Smith"), msg = errormsg)

    def test_election_day_1(self):
        errormsg = 'Failed test_election_day_1'
        election_1 = [["Pepsi", 500, "CA"], ["Coke", 15000, "GA"], ["Pepsi", 3, "GA"], ["Dr. Pepper", 1000, "WY"], ["Coke", 100, "WI"]]
        self.assertEqual("Coke, 15100, GA",
                         hw.election_day(election_1), msg = errormsg)

    def test_election_day_2(self):
        errormsg = 'Failed test_election_day_2'
        election_2 = [["red", 10, "AL"], ["orange", 8, "MI"], ["yellow", 3, "LA"], ["green", 12, "FL"], ["blue", 5, "NJ"]]
        self.assertEqual('green, 12, FL',
                         hw.election_day(election_2), msg = errormsg)

    def test_election_day_3(self):
        errormsg = 'Failed test_election_day_3'
        election_3 = [["McDonald's", 100, "OR"], ["Wendy's", 400, "WA"], ["McDonald's", 25, "ND"], ["Burger King", 45, "KS"], ["Wendy's", 600, "MS"], ["McDonald's", 0, "TN"]]
        self.assertEqual("Wendy's, 1000, MS",
                         hw.election_day(election_3), msg = errormsg)

    def test_add_next_1(self):
        errormsg = 'Failed add_next with [2, 5, 9]'
        things = [2, 5, 9]
        hw.add_next(things)
        self.assertEqual([7, 14, 18], things, msg = errormsg)

    def test_add_next_2(self):
        errormsg = 'Failed add_next with [3]'
        things = [3]
        hw.add_next(things)
        self.assertEqual([6], things, msg = errormsg)
    def test_add_next_3(self):
        errormsg = 'Failed add_next with [-1, 2, 4]'
        things = [-1, 2, 4]
        hw.add_next(things)
        self.assertEqual([1, 6, 8], things, msg = errormsg)

if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW4")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW4.py or file is not in the same directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
