import sys
import unittest
import importlib

"""
Tester for HW11 - CS1301 - Fall 2017
"""


class TestMyClass(unittest.TestCase):

    def test_reverse_phrase_1(self):
        expected = "emit a nopu ecno"
        actual = hw.reverse_phrase('once upon a time')
        self.assertEqual(expected, actual, msg='Failed '
                                               'reverse_phrase '
                                               'with \'emit a nopu ecno\'.')

    def test_reverse_phrase_2(self):
        expected = ''
        actual = hw.reverse_phrase('')
        self.assertEqual(expected, actual, msg='Failed '
                                               'reverse_phrase '
                                               'with \'\'.')

    def test_reverse_phrase_3(self):
        expected = '123 321'
        actual = hw.reverse_phrase('123 321')
        self.assertEqual(expected, actual, msg='Failed '
                                               'reverse_phrase '
                                               'with \'123 321\'.')

    def test_reverse_phrase_4(self):
        expected = 'i am number four'
        actual = hw.reverse_phrase('ruof rebmun ma i')
        self.assertEqual(expected, actual, msg='Failed '
                                               'reverse_phrase '
                                               'with \'ruof rebmun ma i\'.')

    def test_reverse_phrase_5(self):
        expected = 'yay. this is in reverse.'
        actual = hw.reverse_phrase('.esrever ni si siht .yay')
        self.assertEqual(expected, actual, msg='Failed '
                                               'reverse_phrase '
                                               'with \'.esrever ni si siht .yay'
                                               '\'.')

    def test_find_parenthesized_string_1(self):
        expected = '(David, Kelly, Cory)'
        actual = hw.find_parenthesized_string('xsyidlk(David, Kelly, Cory)lkj')
        self.assertEqual(expected, actual, msg='Failed '
                                               'find_parenthesized_string '
                                               'with \'xsyidlk(David, Kelly, '
                                               'Cory)lkj\'.')

    def test_find_parenthesized_string_2(self):
        expected = '(lost)'
        actual = hw.find_parenthesized_string('(lost)')
        self.assertEqual(expected, actual, msg='Failed '
                                               'find_parenthesized_string '
                                               'with \'(lost)\'.')

    def test_find_parenthesized_string_3(self):
        expected = '(hi:P)'
        actual = hw.find_parenthesized_string('abcdefgh;alkdjs(hi:P)')
        self.assertEqual(expected, actual, msg='Failed '
                                               'find_parenthesized_string '
                                               'with \'abcdefgh;alkdjs('
                                               'hi:P)\'.')

    def test_find_parenthesized_string_4(self):
        expected = '(hi:P)'
        actual = hw.find_parenthesized_string('abcdefgh;alkdjs(hi:P)')
        self.assertEqual(expected, actual, msg='Failed '
                                               'find_parenthesized_string '
                                               'with \'abcdefgh;alkdjs('
                                               'hi:P)\'.')

    def test_find_parenthesized_string_5(self):
        expected = '()'
        actual = hw.find_parenthesized_string('xyz()abc123')
        self.assertEqual(expected, actual, msg='Failed '
                                               'find_parenthesized_string '
                                               'with \'xyz()abc123\'.')

    def test_factorial_dictionary_1(self):
        expected = {1: 1}
        actual = hw.factorial_dictionary(1)
        self.assertEqual(expected, actual, msg='Failed '
                                               'factorial_dictionary '
                                               'with \'1\'.')

    def test_factorial_dictionary_2(self):
        expected = {1: 1, 2: 2, 3: 6, 4: 24}
        actual = hw.factorial_dictionary(4)
        self.assertEqual(expected, actual, msg='Failed '
                                               'factorial_dictionary '
                                               'with \'4\'.')

    def test_factorial_dictionary_3(self):
        expected = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}
        actual = hw.factorial_dictionary(6)
        self.assertEqual(expected, actual, msg='Failed '
                                               'factorial_dictionary '
                                               'with \'6\'.')

    def test_factorial_dictionary_4(self):
        expected = {1: 1, 2: 2, 3: 6}
        actual = hw.factorial_dictionary(3)
        self.assertEqual(expected, actual, msg='Failed '
                                               'factorial_dictionary '
                                               'with \'3\'.')

    def test_factorial_dictionary_5(self):
        expected = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320}
        actual = hw.factorial_dictionary(8)
        self.assertEqual(expected, actual, msg='Failed '
                                               'factorial_dictionary '
                                               'with \'3\'.')

    def test_pascal_triangle_1(self):
        expected = [1, 3, 3, 1]
        actual = hw.pascal_triangle(3)
        self.assertEqual(expected, actual, msg='Failed '
                                               'pascal_triangle '
                                               'with \'3\'.')

    def test_pascal_triangle_2(self):
        expected = [1, 8, 28, 56, 70, 56, 28, 8, 1]
        actual = hw.pascal_triangle(8)
        self.assertEqual(expected, actual, msg='Failed '
                                               'pascal_triangle '
                                               'with \'8\'.')

    def test_pascal_triangle_3(self):
        expected = [1, 4, 6, 4, 1]
        actual = hw.pascal_triangle(4)
        self.assertEqual(expected, actual, msg='Failed '
                                               'pascal_triangle '
                                               'with \'4\'.')

    def test_pascal_triangle_4(self):
        expected = [1, 2, 1]
        actual = hw.pascal_triangle(2)
        self.assertEqual(expected, actual, msg='Failed '
                                               'pascal_triangle '
                                               'with \'2\'.')

    def test_pascal_triangle_5(self):
        expected = [1, 7, 21, 35, 35, 21, 7, 1]
        actual = hw.pascal_triangle(7)
        self.assertEqual(expected, actual, msg='Failed '
                                               'pascal_triangle '
                                               'with \'2\'.')


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW11")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".
              format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW5.py or file is not in the same"
              " directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
