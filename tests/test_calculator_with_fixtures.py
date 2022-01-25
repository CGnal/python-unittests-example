
import unittest
from app.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        '''Set up an instance of Calculator pior to every test execution'''
        self.calc = Calculator()

    def test_div(self):
        '''Test case function for division'''
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(12, 2), 6)

    def test_div_error(self):
        '''Make sure ZeroDivisionError is raised when necessary'''
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)
