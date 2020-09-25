import sys
import unittest
import importlib
import os
"""
Autograder for HW05 - CS1301 - Fall 2017
"""

class TestMyClass(unittest.TestCase):

    def test_complex_calculator_1(self):
        self.assertEqual(None, hw.complex_calculator('code', [1, 2, 3]), msg="Failed complex_calculator w/ 'code' and [1, 2, 3].")


    def test_complex_calculator_2(self):
        self.assertEqual(8.0, hw.complex_calculator('pow', [2, 3]), msg="Failed complex_calculator w/ 'pow' and [2, 3].")


    def test_complex_calculator_3(self):
        self.assertEqual(0.909, hw.complex_calculator('sin', [2]), msg="Failed complex_calculator w/ 'sin' and [2].")


    def test_complex_calculator_4(self):
        self.assertEqual(192.0, hw.complex_calculator('fabs', [-192]), msg="Failed complex_calculator w/ 'fabs' and [-192].")


    def test_complex_calculator_5(self):
        self.assertEqual(5, hw.complex_calculator('gcd', [125, 1940]), msg="Failed complex_calculator w/ 'gcd' and [125, 1940].")


    def test_complex_calculator_6(self):
        self.assertEqual(22, hw.complex_calculator('ceil', [21.2]), msg="Failed complex_calculator w/ 'ceil' and [21.2].")

    def test_help_recruit_1(self):
        self.assertEqual(('Football', 1, 'TaQuon Marshall'), hw.help_recruit("TaQuon Marshall: Football, 1"), msg="Failed help_recruit w/ 'TaQuon Marshall: Football, 1'.")


    def test_help_recruit_2(self):
        self.assertEqual(('Basketball', 2, 'Ben Lammers'), hw.help_recruit("Ben Lammers: Basketball, 2"), msg="Failed help_recruit w/ 'Ben Lammers: Basketball, 2'.")


    def test_help_recruit_3(self):
        self.assertEqual(('Volleyball', 6, 'Kelsey Chisholm'), hw.help_recruit("Kelsey Chisholm: Volleyball, 6"), msg="Failed help_recruit w/ 'Kelsey Chisholm: Volleyball, 6'.")


    def test_help_recruit_4(self):
        self.assertEqual(('Swimming', 11, 'Alex Rieger'), hw.help_recruit("Alex Rieger: Swimming, 11"), msg="Failed help_recruit w/ 'Alex Rieger: Swimming, 11'.")


    def test_help_recruit_5(self):
        self.assertEqual(('Tennis', 3, 'Andrew Li'), hw.help_recruit("Andrew Li: Tennis, 3"), msg="Failed help_recruit w/ 'Andrew Li: Tennis, 3'.")


    def test_recruiting_profile_1(self):
        self.assertEqual([(1, 'Tennis', 'Chris Eubanks'), (2, 'Tennis', 'Andrew Li'), (3, 'Tennis', 'Daniel Yun')], hw.recruiting_profile(["Jair Anderson: Football, 4","TaQuon Marshall: Football, 1", "Daniel Yun: Tennis, 3",
                              "Gabby Benda: Volleyball, 7","Ashley Askin: Volleyball, 2",
                              "Sydney Wilson: Volleyball, 5", "Chris Eubanks: Tennis, 1", "Zach Matthews: Football, 11", "Andrew Li: Tennis, 2"], "Tennis"), msg='''Failed recruiting_profile w/ ["Jair Anderson: Football, 4","TaQuon Marshall: Football, 1", "Daniel Yun: Tennis, 3",
                              "Gabby Benda: Volleyball, 7","Ashley Askin: Volleyball, 2",
                              "Sydney Wilson: Volleyball, 5", "Chris Eubanks: Tennis, 1", "Zach Matthews: Football, 11", "Andrew Li: Tennis, 2"], "Tennis".''')


    def test_recruiting_profile_2(self):
        self.assertEqual([(2, 'Swimming', 'Matt Casillas'), (5, 'Swimming', 'Megan Hansen'), (7, 'Swimming', 'Megan Young'), (8, 'Swimming', 'Brad Oberg')], hw.recruiting_profile(["Wade Bailey: Baseball, 3", "Josh Okogie: Basketball, 1",
                               "Tadric Jackson: Basketball, 4","Megan Young: Swimming, 7",
                               "Ben Lammers: Basketball, 2","Jake Lee: Baseball, 8","Brad Oberg: Swimming, 8",
                               "Megan Hansen: Swimming, 5","Joey Bart: Baseball, 5", "Matt Casillas: Swimming, 2"], "Swimming"), msg='''Failed recruiting_profile w/ ["Wade Bailey: Baseball, 3", "Josh Okogie: Basketball, 1",
                               "Tadric Jackson: Basketball, 4","Megan Young: Swimming, 7",
                               "Ben Lammers: Basketball, 2","Jake Lee: Baseball, 8","Brad Oberg: Swimming, 8",
                               "Megan Hansen: Swimming, 5","Joey Bart: Baseball, 5", "Matt Casillas: Swimming, 2"], "Swimming".''')


    def test_recruiting_profile_3(self):
        self.assertEqual([(3, 'Track and Field', 'Matt Munns'), (6, 'Track and Field', 'Ryan Thomas'), (9, 'Track and Field', 'Matt McBrien')], hw.recruiting_profile(["Nami Otsuka: Tennis, 1", "Matt McBrien: Track and Field, 9","Paige Hourigan: Tennis, 2","Katie Krzus: Softball, 6",
                             "Kendall Chadwick: Softball, 4","Kenya Jones: Tennis, 3", "Emily Anderson: Softball, 11","Matt Munns: Track and Field, 3", "Ryan Thomas: Track and Field, 6"], "Track and Field"), msg='''Failed help_recruiting w/ ["Nami Otsuka: Tennis, 1", "Matt McBrien: Track and Field, 9","Paige Hourigan: Tennis, 2","Katie Krzus: Softball, 6", "Kendall Chadwick: Softball, 4","Kenya Jones: Tennis, 3", "Emily Anderson: Softball, 11","Matt Munns: Track and Field, 3",
                             "Ryan Thomas: Track and Field, 6"], "Track and Field".''')



    def test_recruiting_profile_4(self):
        self.assertEqual([], hw.recruiting_profile(["Lauren Frerking: Volleyball, 11","James Clark: Golf, 3", "Michael Pisciotta: Golf, 2" ], "Tennis"), msg='''Failed help_recruiting w/ ["Lauren Frerking: Volleyball, 11","James Clark: Golf, 3", "Michael Pisciotta: Golf, 2" ], "Tennis".''')




    def test_precious_pets_1(self):
        self.assertEqual(('Fur', 50), hw.precious_pets("Fur, 50 + Ploop, 2 + Fluff, 25"), msg="Failed precious_pets w/ 'Fur, 50 + Ploop, 2 + Fluff, 25'")


    def test_precious_pets_2(self):
        self.assertEqual(('Pumpkin', 900), hw.precious_pets("Pumpkin, 900"), msg="Failed precious_pets  w/ 'Pumpkin, 900'")


    def test_precious_pets_3(self):
        self.assertEqual(('Eve', 20), hw.precious_pets("Jelly, 20 + Bounce, 20 + Eve, 20"), msg="Failed precious_pets w/ 'Jelly, 20 + Bounce, 20 + Eve, 20'")


    def test_precious_pets_4(self):
        self.assertEqual(('Plato', 100), hw.precious_pets("Ploop, 30 + Taurus, 25 + Plato, 100"), msg="Failed precious_pets w/ 'Ploop, 30 + Taurus, 25 + Plato, 100'")


    def test_precious_pets_5(self):
        self.assertEqual(('Socrates', 100), hw.precious_pets("Socrates, 100 + Leo, 99 + Happy, 99"), msg="Failed precious_pets w/ 'Socrates, 100 + Leo, 99 + Happy, 99'")


    def test_hungry_puppies_1(self):
        self.assertEqual((True, 31.5, 'Buster'), hw.hungry_puppies([("Scott", 15.0, 1), ("Buster", 3, 14.0), (10.0, "Gru", 7)], 7.2, 500.0), msg='Failed hungry_puppies w/ [("Scott", 1, 15.0), ("Buster", 3, 14.0), ("Gru", 7, 10.0)], 7.2, 500.0')


    def test_hungry_puppies_2(self):
        self.assertEqual((True, 19.5, 'Blimp'), hw.hungry_puppies([("Blimp", 15.0, 1), (1, 14.0, "Jell"), (1, "Gel", 10.0)], 1.2, 30.0), msg='Failed hungry_puppies w/ [("Blimp", 1, 15.0), ("Jell", 1, 14.0), ("Gel", 1, 10.0)], 1.2, 30.0')


    def test_hungry_puppies_3(self):
        self.assertEqual((False, 29.9, 'Plum'), hw.hungry_puppies([("Blump", 1, 9.0), (14.9, "Plum", 3), ("Peach", 2, 10.5)], 3.4, 70.0), msg='Failed hungry_puppies w/ [("Blump", 1, 9.0), ("Plum", 3, 14.9), ("Peach", 2, 10.5)], 3.4, 70.0')


    def test_hungry_puppies_4(self):
        self.assertEqual((True, 18.0, 'Skittle'), hw.hungry_puppies([(8, "Oreo", 7.6), ("Skittle", 5, 8.9), ("M&M", 3.0, 1)], 6.0, 200.0), msg='Failed hungry_puppies w/ [("Oreo", 8, 7.6), ("Skittle", 5, 8.9), ("M&M", 1, 3.0)], 6.0, 200.0')


    def test_hungry_puppies_5(self):
        self.assertEqual((True, 19.4, 'Git'), hw.hungry_puppies([("Buster", 4, 3.0), (3, 12.3, "Git"), (4.1, "Hub", 12)], 3.2, 87), msg='Failed hungry_puppies w/ [("Buster", 4, 3.0), ("Git", 3, 12.3), ("Hub", 12, 4.1)], 3.2, 87')


    def test_test_release_1(self):
        self.assertEqual([('Dwight', 85.47)], hw.test_release([(80.0, 78.4, 98.0, "Dwight")]), msg='Failed test_release w/ [(80.0, 78.4, 98.0, "Dwight")]')


    def test_test_release_2(self):
        self.assertEqual([('Fred', 89.47), ('Jasmine', 99.03), ('Emily', 98.87)], hw.test_release([(80.0, 98.4, 90.0, "Fred"), (99.3, 100.0, 97.8, "Jasmine"), ("Emily", 96.8, 99.8, 100.0)]), msg='Failed test_release w/ [(80.0, 98.4, 90.0, "Fred"), (99.3, 100.0, 97.8, "Jasmine"), ("Emily", 96.8, 99.8, 100.0)]')


    def test_test_release_3(self):
        self.assertEqual([('Oswell', 98.6), ('Oswald', 90.43)], hw.test_release([("Joey",), (97.8, "Oswell", 99.0, 99.0), ("Oswald", 89.7, 82.4, 99.2)]), msg='Failed test_release w/ [("Joey",), (97.8, "Oswell", 99.0, 99.0), ("Oswald", 89.7, 82.4, 99.2)]')


    def test_test_release_4(self):
        self.assertEqual([('Caroline', 100.0), ('David', 100.0)], hw.test_release([("Leslie", 60.0), (100.0, 100.0, "Caroline", 100.0), (100.0, "David", 100.0, 100.0)]), msg='Failed test_release w/ [("Leslie", 60.0), (100.0, 100.0, "Caroline", 100.0), (100.0, "David", 100.0, 100.0)]')


    def test_test_release_5(self):
        self.assertEqual([('Daniel', 46.2), ('Chris', 62.67)], hw.test_release([(34.8, 23.4, 80.4, "Daniel"), (23.5, 96.5, 68.0, "Chris"), ("Sweta", 100.0, 99.0)]), msg='Failed test_release w/ [(34.8, 23.4, 80.4, "Daniel"), (23.5, 96.5, 68.0, "Chris"), ("Sweta", 100.0, 99.0)]')

if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW5")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW5.py or file is not in the same directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
