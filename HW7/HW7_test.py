import sys
import unittest
import importlib
import os
"""
Autograder for HW07 - CS1301 - Spring 2017
"""

class TestMyClass(unittest.TestCase):

    def test_scheduler_1(self):
        info_dict_1 = {"Andrew Andrews": [1,4,7,8], "Brock Brockson": [1,6,8,12], "Charles Charleston": [1,2,3], "David Davidson": [1,5,9,10], "Ellen Ellenson": [1]}
        self.assertEqual('January', hw.scheduler(info_dict_1), msg='Failed scheduler w/ {"Andrew Andrews": [1,4,7,8], "Brock Brockson": [1,6,8,12], "Charles Charleston": [1,2,3], "David Davidson": [1,5,9,10], "Ellen Ellenson": [1]}.')

    def test_scheduler_2(self):
        info_dict_2 = {"Flora Flores": [4,5,6,3], "George Georges": [4,5,6,3], "Henry Henries": [4,5,6,3], "Isabella Isbell": [4,5,6,3], "John Johnson": [4,5,6,3]}
        self.assertEqual('March', hw.scheduler(info_dict_2), msg='Failed scheduler w/ {Flora Flores": [4,5,6,3], "George Georges": [4,5,6,3], "Henry Henries": [4,5,6,3], "Isabella Isbell": [4,5,6,3], "John Johnson": [4,5,6,3]}.')

    def test_scheduler_3(self):
        info_dict_3 = {"Karl Karlson": [4,5,6,7], "Ling Ling": [8,9,10,11]}
        self.assertEqual('April', hw.scheduler(info_dict_3), msg='Failed scheduler w/ {"Karl Karlson": [4,5,6,7], "Ling Ling": [8,9,10,11]}.')

    def test_scheduler_4(self):
        info_dict_4 = {"Michael Michaelson": [], "Nancy Nancies": []}
        self.assertEqual('January', hw.scheduler(info_dict_4), msg='Failed scheduler w/ {"Michael Michaelson": [], "Nancy Nancies": []}.')

    def test_scheduler_5(self):
        info_dict_5 = {"Oliver Oliver": [5], "Pearl Pearlson": []}
        self.assertEqual('May', hw.scheduler(info_dict_5), msg='Failed scheduler w/ {"Oliver Oliver": [5], "Pearl Pearlson": []}.')


    def test_buy_albums_1(self):
        self.assertEqual({'total': 0}, hw.buy_albums({},{}), msg="Failed buy_albums w/ {} and {}")

    def test_buy_albums_2(self):
        self.assertEqual({'total': 0}, hw.buy_albums({},{'Kid Cudi':7.50}), msg="Failed buy_albums w/ {} and {'Kid Cudi':7.50}")

    def test_buy_albums_3(self):
        self.assertEqual({'Mura Masa':12.36, 'total':12.36}, hw.buy_albums({'Mura Masa':'Mura Masa', 'Soundtrack to a Death':'Mura Masa'},{'Mura Masa':6.18}), msg="Failed buy_albums w/ {'Mura Masa':'Mura Masa', 'Soundtrack to a Death':'Mura Masa'} and {'Mura Masa':6.18}")

    def test_buy_albums_4(self):
        self.assertEqual({'Lupe Fiasco':10.00, 'Magic City Hippies':3.25, 'J. Cole':16.50, 'total':29.75}, hw.buy_albums({'Tetsuo & Youth':'Lupe Fiasco', 'Lasers':'Lupe Fiasco', 'Hippie Castle EP':'Magic City Hippies', '2014 Forest Hills Drive':'J. Cole', 'Friday Night Lights':'J. Cole'}, {'Lupe Fiasco':5.00, 'Magic City Hippies':3.25, 'J. Cole':8.25}), msg="Failed buy_albums w/ {'Tetsuo & Youth':'Lupe Fiasco', 'Lasers':'Lupe Fiasco', 'Hippie Castle EP':'Magic City Hippies', '2014 Forest Hills Drive':'J. Cole', 'Friday Night Lights':'J. Cole'} and {'Lupe Fiasco':5.00, 'Magic City Hippies':3.25, 'J. Cole':8.25}")

    def test_buy_albums_5(self):
        self.assertEqual({'Chance the Rapper':0.00, 'Kanye West':19.98, 'Frank Ocean':99.99, 'total':119.97}, hw.buy_albums({'10 Day':'Chance the Rapper', 'Acid Rap':'Chance the Rapper', 'Coloring Book':'Chance the Rapper', 'Graduation':'Kanye West', 'The Life of Pablo':'Kanye West', 'Endless':'Frank Ocean'},{'Chance the Rapper':0.00, 'Kanye West':9.99, 'Frank Ocean':99.99, 'Jay Prince':11.15}), msg="Failed buy_albums w/ {'10 Day':'Chance the Rapper', 'Acid Rap':'Chance the Rapper', 'Coloring Book':'Chance the Rapper', 'Graduation':'Kanye West', 'The Life of Pablo':'Kanye West', 'Endless':'Frank Ocean'} and {'Chance the Rapper':0.00, 'Kanye West':9.99, 'Frank Ocean':99.99, 'Jay Prince':11.15}")


    def test_translator_1(self):
        errormsg = 'Failed translator with french_dictionary.txt and "hello, my name is christine! my favorite food is pizza."'
        actual = hw.translator('french_dictionary.txt', 'hello, my name is christine! my favorite food is pizza.')
        expected = 'bonjour, mon nom est chresttine! mon favorite food est pizza.'
        self.assertEqual(expected, actual, msg=errormsg)

    def test_translator_2(self):
        errormsg = 'Failed translator with german_dictionary.txt and "i read many books. i study math and computer science."'
        actual = hw.translator('german_dictionary.txt', 'i read many books. i study math and computer science.')
        expected = 'ich lebe viele Bucher. ich studiere Mathematik und computer scichence.'
        self.assertEqual(expected, actual, msg=errormsg)

    def test_translator_3(self):
        errormsg = 'Failed translator with spanish_dictionary.txt and "hello, my name is christine! my favorite food is pizza."'
        actual = hw.translator('spanish_dictionary.txt', 'i want new friends now. i have ten dogs and five cats')
        expected = 'yo quiero nuevos fryoends ahora. yo tengo diez perros and fyove gatos'
        self.assertEqual(expected, actual, msg=errormsg)

    def test_translator_4(self):
        errormsg = 'Failed translator with number_dictionary.txt and "three thousand four hundred and twenty-six"'
        actual = hw.translator('number_dictionary.txt', 'three thousand four hundred and twenty-six')
        expected = '3 1000 4 100 and twenty-6'
        self.assertEqual(expected, actual, msg=errormsg)

    def test_translator_5(self):
        errormsg = 'Failed translator with opposite_dictionary.txt and "you are very boring. you hate python!"'
        actual = hw.translator('opposite_dictionary.txt', 'i am very fun. i love python!')
        expected = 'you are very boring. you hate python!'
        self.assertEqual(expected, actual, msg=errormsg)

    def test_average_rating_1(self):
        self.assertEqual({}, hw.average_rating({}), msg="Failed average_rating w/ {}")

    def test_average_rating_2(self):
        self.assertEqual({'The Pursuit of Happyness':9.99}, hw.average_rating({'The Pursuit of Happyness':[9.98,10.0]}), msg="Failed average_rating w/ {'The Pursuit of Happyness':[9.98,10.00]}")

    def test_average_rating_3(self):
        self.assertEqual({'I Am Legend':8.00, 'The Karate Kid':7.25}, hw.average_rating({'I Am Legend':[7.0,9.0], 'The Karate Kid':[7.25,7.3,7.25,7.2]}), msg="Failed average_rating w/ {'I Am Legend':[7.0,9.0], 'The Karate Kid':[7.25,7.3,7.25,7.2]}")


    def test_average_rating_4(self):
        self.assertEqual({'Batman Begins':10.0}, hw.average_rating({'Batman Begins':[10.0]}), msg="Failed average_rating w/ {'Batman Begins':[10.0]}.")

    def test_average_rating_5(self):
        self.assertEqual({'Looper':6.67, 'Jumper':4.5, 'The Fifth Element':9.0}, hw.average_rating({'Looper':[7.0,8.0,5.0], 'Jumper':[3.0,6.0], 'The Fifth Element':[9.00]}), msg="Failed average_rating w/ {'Looper':[7.0,8.0,5.0], 'Jumper':[3.0,6.0], 'The Fifth Element':[9.00]}.")


    def test_sentence_stats_1(self):
        actual = hw.sentence_stats("Hello! My name is Christine 07/08")
        expected = {'uppercase': 3, 'lowercase': 19, 'vowels': 8, 'consonants': 14, 'numbers': 4, 'special_chars': 2, 'word_count': 6, 'most_common': 'e'}
        self.assertEqual(expected, actual, msg="Failed sentence_stats w/ 'Hello! My name is Christine 07/08'.")

    def test_sentence_stats_2(self):
        actual = hw.sentence_stats("!!!#$@%^^&$%^%^$@!%$#%$%&@%$#@%$@")
        expected = {'uppercase': 0, 'lowercase': 0, 'vowels': 0, 'consonants': 0, 'numbers': 0, 'special_chars': 33, 'word_count': 1, 'most_common': '%'}
        self.assertEqual(expected, actual, msg="Failed sentence_stats w/ '!!!#$@%^^&$%^%^$@!%$#%$%&@%$#@%$@'.")

    def test_sentence_stats_3(self):
        actual = hw.sentence_stats("1, 2, 3, 4, 5")
        expected = {'uppercase': 0, 'lowercase': 0, 'vowels': 0, 'consonants': 0, 'numbers': 5, 'special_chars': 4, 'word_count': 5, 'most_common': ','}
        self.assertEqual(expected, actual, msg="Failed sentence_stats w/ '1, 2, 3, 4, 5'.")

    def test_sentence_stats_4(self):
        actual = hw.sentence_stats("cwm fjord bank glyphs vext quiz CWM FJORD BANK GLYPHS VEXT QUIZ")
        expected = {'uppercase': 26, 'lowercase': 26, 'vowels': 10, 'consonants': 42, 'numbers': 0, 'special_chars': 0, 'word_count': 12, 'most_common': 'c'}
        self.assertEqual(expected, actual, msg="Failed sentence_stats w/ 'cwm fjord bank glyphs vext quiz CWM FJORD BANK GLYPHS VEXT QUIZ'.")

    def test_sentence_stats_5(self):
        actual = hw.sentence_stats("Mr. Jock, TV quiz PhD, bags few lynx")
        expected = {'uppercase': 6, 'lowercase': 20, 'vowels': 5, 'consonants': 21, 'numbers': 0, 'special_chars': 3, 'word_count': 8, 'most_common': ','}
        self.assertEqual(expected, actual, msg="Failed sentence_stats w/ 'Mr. Jock, TV quiz PhD, bags few lynx'.")


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW7")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW7.py or file is not in the same directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
