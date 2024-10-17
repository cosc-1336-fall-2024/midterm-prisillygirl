#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_random_number
from src.question_b.question_b import test_config
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_question_b_config(self):
        self.assertEqual(True, test_config())

    def test_question_c_config(self):
        self.assertEqual(True, test_config())


#testing question a 
def test_get_sum_of_evens(self):
    self.assertEqual(30, test_get_sum_of_evens(11))
    self.assertEqual(30, test_get_sum_of_evens(10))
    self.assertEqual(8, test_get_sum_of_evens(20))

#testing question b
def test_get_fahrenheit(self):
    self.assertEqual(32, test_get_fahrenheit(0))
    self.assertEqual(41, test_get_fahrenheit(5))
    self.assertEqual(50, test_get_fahrenheit(10))


#testing question c
def test_get_random_number(self): 
      for i in range(0, 5):
        number = get_random_number(1, 5)
        self.assertEqual(True, (number >= 1))
        self.assertEqual(True, (number <= 5))







