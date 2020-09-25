import sys
import unittest
import os
import importlib
"""
STUDENT autograder for HW06 - CS1301
"""

__author__ = "Caroline Kish and David Wang"
__version__ = "1.0"
__email__ = "ckish3@gatech.edu and dwang388@gatech.edu"

class TestMyClass(unittest.TestCase):
    def test_affordable_homes_1(self):
        errormsg = 'Failed affordable_homes with 900000, 3849, 4, "homes1.txt"'
        hw.affordable_homes(900000, 3849, 4, 'homes1.txt')
        self.assertTrue(os.path.isfile("homes1.txt"), msg="homes1.txt does not exist")
        handle = open("homes1.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("1. Address: 14151 INDIO DR\n\tCost: $2000.0\n2. Address: 5201 BLOSSOM RANCH DR\n\tCost: "
                         "$450000.0\n3. Address: 3027 PALMATE WAY\n\tCost: $452000.0\n4. Address: 9760 LAZULITE "
                         "CT\n\tCost: $460000.0\n", content, msg=errormsg)

    def test_affordable_homes_2(self):
        errormsg = 'Failed affordable_homes with 0, 100000, 10, "homes2.txt"'
        hw.affordable_homes(0, 100000, 10, 'homes2.txt')
        self.assertTrue(os.path.isfile("homes2.txt"), msg="homes2.txt does not exist")
        handle = open("homes2.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("", content, msg=errormsg)

    def test_affordable_homes_3(self):
        errormsg = 'Failed affordable_homes with 900000, 3300, 4, "homes3.txt"'
        hw.affordable_homes(900000, 3300, 4, 'homes3.txt')
        self.assertTrue(os.path.isfile("homes3.txt"), msg="homes3.txt does not exist")
        handle = open("homes3.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("1. Address: 14151 INDIO DR\n\tCost: $2000.0\n2. Address: 2912 NORCADE CIR\n\tCost: "
                         "$282400.0\n3. Address: 4359 CREGAN CT\n\tCost: $320000.0\n4. Address: 5912 DEEPDALE "
                         "WAY\n\tCost: $320000.0\n", content, msg=errormsg)

    def test_affordable_homes_4(self):
        errormsg = 'Failed affordable_homes with 200000, 1100, 15, "homes4.txt"'
        hw.affordable_homes(200000, 1100, 15, 'homes4.txt')
        self.assertTrue(os.path.isfile("homes4.txt"), msg="homes4.txt does not exist")
        handle = open("homes4.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("1. Address: 14151 INDIO DR\n\tCost: $2000.0\n2. Address: 8208 WOODYARD WAY\n\tCost: "
                         "$30000.0\n3. Address: 7401 TOULON LN\n\tCost: $56950.0\n4. Address: 51 OMAHA CT\n\tCost: "
                         "$68212.0\n5. Address: 83 ARCADE BLVD\n\tCost: $80000.0\n6. Address: 3845 ELM ST\n\tCost: "
                         "$84000.0\n7. Address: 483 ARCADE BLVD\n\tCost: $89000.0\n8. Address: 5828 PEPPERMILL "
                         "CT\n\tCost: $89921.0\n9. Address: 671 SONOMA AVE\n\tCost: $90000.0\n10. Address: 6048 OGDEN "
                         "NASH WAY\n\tCost: $90895.0\n11. Address: 2561 19TH AVE\n\tCost: $91002.0\n12. Address: 4113 "
                         "DAYSTAR CT\n\tCost: $93600.0\n13. Address: 1069 ACACIA AVE\n\tCost: $98000.0\n14. Address: "
                         "7325 10TH ST\n\tCost: $98937.0\n15. Address: 3847 LAS PASAS WAY\n\tCost: $99000.0\n",
                         content, msg=errormsg)

    def test_affordable_homes_5(self):
        errormsg = 'Failed affordable_homes with 300000, 2200, 1, "homes5.txt"'
        hw.affordable_homes(300000, 2200, 1, 'homes5.txt')
        self.assertTrue(os.path.isfile("homes5.txt"), msg="homes5.txt does not exist")
        handle = open("homes5.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("1. Address: 14151 INDIO DR\n\tCost: $2000.0\n", content, msg=errormsg)

    def test_sold_day_1(self):
        errormsg = 'Failed sold_day with "Wed"'
        self.assertEqual(158, hw.sold_day("Wed"), msg=errormsg)

    def test_sold_day_2(self):
        errormsg = 'Failed sold_day with "Thu"'
        self.assertEqual(118, hw.sold_day("Thu"), msg=errormsg)

    def test_sold_day_3(self):
        errormsg = 'Failed sold_day with "Day"'
        self.assertEqual(-1, hw.sold_day("Day"), msg=errormsg)

    def test_home_profile_1(self):
        errormsg = 'Failed home_profile with 8001 HARTWICK WAY and True'
        hw.home_profile('8001 HARTWICK WAY', True)
        self.assertTrue(os.path.isfile("profileFile.txt"), msg="profileFile.txt does not exist")
        handle = open("profileFile.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Address:\n8001 HARTWICK WAY\nSACRAMENTO, CA\nRooms:\n4 beds, 2 baths\n\n", content, msg=errormsg)

    def test_home_profile_2(self):
        errormsg = 'Failed home_profile with 15300 MURIETA SOUTH PKWY and False'
        hw.home_profile('15300 MURIETA SOUTH PKWY', False)
        self.assertTrue(os.path.isfile("profileFile.txt"), msg="profileFile.txt does not exist")
        handle = open("profileFile.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Address:\n8001 HARTWICK WAY\nSACRAMENTO, CA\nRooms:\n4 beds, 2 baths\n\nAddress:\n15300"
                         " MURIETA SOUTH PKWY\nRANCHO MURIETA, CA\nRooms:\n4 beds, 3 baths\n\n", content,
                         msg=errormsg)

    def test_home_profile_2(self):
        errormsg = 'Failed home_profile with 15300 MURIETA SOUTH PKWY and False'
        hw.home_profile('15300 MURIETA SOUTH PKWY', False)
        self.assertTrue(os.path.isfile("profileFile.txt"), msg="profileFile.txt does not exist")
        handle = open("profileFile.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Address:\n8001 HARTWICK WAY\nSACRAMENTO, CA\nRooms:\n4 beds, 2 baths\n\nAddress:\n15300"
                         " MURIETA SOUTH PKWY\nRANCHO MURIETA, CA\nRooms:\n4 beds, 3 baths\n\n", content,
                         msg=errormsg)

    def test_home_profile_3(self):
        errormsg = 'Failed home_profile with 20 and True'
        hw.home_profile('20', True)
        self.assertTrue(os.path.isfile("profileFile.txt"), msg="profileFile.txt does not exist")
        handle = open("profileFile.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Address:\n20\nSACRAMENTO, CA\nRooms:\n3 beds, 2 baths\n\n", content,
                         msg=errormsg)

    def test_make_roster_1(self):
        errormsg = 'Failed make_roster with "Benjamin Wellington, Caroline Kish, Catherine Liu" and "out1.txt"'
        hw.make_roster("Benjamin Wellington, Caroline Kish, Catherine Liu", "out1.txt")
        self.assertTrue(os.path.isfile("out1.txt"), msg="out1.txt does not exist")
        handle = open("out1.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Kish, Caroline\nLiu, Catherine\nWellington, Benjamin", content, msg=errormsg)

    def test_make_roster_2(self):
        errormsg = 'Failed make_roster with "Cory Brooks, Christine Feng, Daniel Marcos" and "out2.txt"'
        hw.make_roster("Cory Brooks, Christine Feng, Daniel Marcos", "out2.txt")
        self.assertTrue(os.path.isfile("out2.txt"), msg="out2.txt does not exist")
        handle = open("out2.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Brooks, Cory\nFeng, Christine\nMarcos, Daniel", content, msg=errormsg)

    def test_make_roster_3(self):
        errormsg = 'Failed make_roster with "David Wang, Elena May, Erica Chia" and "out3.txt"'
        hw.make_roster("David Wang, Elena May, Erica Chia", "out3.txt")
        self.assertTrue(os.path.isfile("out3.txt"), msg="out3.txt does not exist")
        handle = open("out3.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Chia, Erica\nMay, Elena\nWang, David", content, msg=errormsg)

    def test_make_roster_4(self):
        errormsg = 'Failed make_roster with "John Wood, Kelly Zou, Lucille Wang, Marcus Wilder, Nicolas Rodrguez, ' \
                   'Nikita Bawa, Rodrigo Mejia, Soni Aggarwal, Tiffany Xu" and "out4.txt"'
        hw.make_roster("John Wood, Kelly Zou, Lucille Wang, Marcus Wilder, Nicolas Rodrguez, Nikita Bawa, "
                       "Rodrigo Mejia, Soni Aggarwal, Tiffany Xu", "out4.txt")
        self.assertTrue(os.path.isfile("out4.txt"), msg="out4.txt does not exist")
        handle = open("out4.txt")
        content = handle.read()
        handle.close()
        self.assertEqual("Aggarwal, Soni\nBawa, Nikita\nMejia, Rodrigo\nRodrguez, Nicolas\nWang, Lucille\nWilder, "
                         "Marcus\nWood, John\nXu, Tiffany\nZou, Kelly", content, msg=errormsg)

    def test_choose_group_1(self):
        errormsg = "Failed choose_group with ['Caroline', 'Katie', 'Molly', 'Patricia', 'Daniel'], 0, and " \
                   " 'test_choose_group_1.txt' "
        hw.choose_group(['Caroline', 'Katie', 'Molly', 'Patricia', 'Daniel'], 0, 'test_choose_group_1.txt')
        self.assertTrue(os.path.isfile("test_choose_group_1.txt"), msg="test_choose_group_1.txt does not exist")
        handle = open('test_choose_group_1.txt')
        content = handle.read()
        handle.close()
        self.assertEqual("", content, msg=errormsg)

    def test_choose_group_2(self):
        errormsg = "Failed choose_group with ['Oscar', 'Biscuit', 'Sirius'], 4, and 'test_choose_group_2.txt' "
        hw.choose_group(['Oscar', 'Biscuit', 'Sirius'], 4, 'test_choose_group_2.txt')
        self.assertTrue(os.path.isfile("test_choose_group_2.txt"), msg="test_choose_group_2.txt does not exist")
        handle = open('test_choose_group_2.txt')
        content = handle.read()
        handle.close()
        self.assertEqual("Not enough people for a group.", content, msg=errormsg)

    def test_choose_group_3(self):
        errormsg = "Failed choose_group with ['Katniss', 'Peeta', 'Gale', 'Tris', 'Percy'], 3, and " \
                   "'test_choose_group_3.txt' "
        hw.choose_group(['Katniss', 'Peeta', 'Gale', 'Tris', 'Percy'], 3, 'test_choose_group_3.txt')
        self.assertTrue(os.path.isfile("test_choose_group_3.txt"), msg="test_choose_group_3.txt does not exist")
        handle = open('test_choose_group_3.txt')
        content = handle.read()
        handle.close()
        self.assertEqual("Team: Percy, Tris, Gale", content, msg=errormsg)

    def test_choose_group_4(self):
        errormsg = "Failed choose_group with ['Person One'], 1, and " \
                   "'test_choose_group_4.txt' "
        hw.choose_group(['Person One'], 1, 'test_choose_group_4.txt')
        self.assertTrue(os.path.isfile("test_choose_group_4.txt"), msg="test_choose_group_4.txt does not exist")
        handle = open('test_choose_group_4.txt')
        content = handle.read()
        handle.close()
        self.assertEqual("Team: Person One", content, msg=errormsg)

    def test_get_roster_1(self):
        errormsg = 'Failed get_roster with "scores1.txt'
        self.assertEqual(['Iron Man', 'Hulk', 'Captain America'], hw.get_roster("scores1.txt"), msg=errormsg)

    def test_get_roster_2(self):
        errormsg = 'Failed get_roster with "scores2.txt'
        self.assertEqual(['Batman', 'Wonder Woman', 'Superman'], hw.get_roster("scores2.txt"), msg=errormsg)

    def test_get_roster_3(self):
        errormsg = 'Failed get_roster with "scores3.txt'
        self.assertEqual(['Student1', 'Student2', 'Student3', 'Student4'], hw.get_roster("scores3.txt"), msg=errormsg)

    def test_tests_missed_1(self):
        errormsg = 'Failed tests_missed with "scores1.txt'
        self.assertEqual([4, 5], hw.tests_missed("scores1.txt"), msg=errormsg)

    def test_tests_missed_2(self):
        errormsg = 'Failed tests_missed with "scores2.txt'
        self.assertEqual([4, 5, 2, 3, 5], hw.tests_missed("scores2.txt"), msg=errormsg)

    def test_tests_missed_3(self):
        errormsg = 'Failed tests_missed with "scores2.txt'
        self.assertEqual([11, 2], hw.tests_missed("scores3.txt"), msg=errormsg)

    def test_find_avg_1(self):
        errormsg = 'Failed find_avg with "scores1.txt" and "Hulk"'
        self.assertEqual(94.34, hw.find_avg("scores1.txt", "Hulk"), msg=errormsg)

    def test_find_avg_2(self):
        errormsg = 'Failed find_avg with "scores2.txt" and "Superman"'
        self.assertEqual(93.9, hw.find_avg("scores2.txt", "Superman"), msg=errormsg)

    def test_find_avg_3(self):
        errormsg = 'Failed find_avg with "scores3.txt" and "Student3"'
        self.assertEqual(79.12, hw.find_avg("scores3.txt", "Student3"), msg=errormsg)

    def test_find_avg_4(self):
        errormsg = 'Failed find_avg with "scores2.txt" and "Student1"'
        self.assertEqual(0, hw.find_avg("scores2.txt", "Student1"), msg=errormsg)


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW6")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW6.py or file is not in the same directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
