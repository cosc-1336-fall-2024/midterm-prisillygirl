#write function tests here, don't add input('') statements here!
import unittest

from src.question_a.question_a import test_config
from src.question_a.question_a import get_sum_of_evens
from src.question_b.question_b import get_fahrenheit
from src.question_c.question_c import get_random_number
from src.question_d.question_d import get_bonus_pay_amount



#follow this example to add questions b, c, and d for testing including their functions
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_question_b_config(self):
        self.assertEqual(True, test_config())
    
    def test_question_c_config(self):
        self.assertEqual(True, test_config())

    def test_question_d_config(self):
        self.assertEqual(True, test_config())
    
#testing question a 
    def test_get_sum_of_evens(self):
        self.assertEqual(30, get_sum_of_evens(11))
        self.assertEqual(30, get_sum_of_evens(10))
        self.assertEqual(20, get_sum_of_evens(8))

#testing question b
    def test_get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
        self.assertEqual(41, get_fahrenheit(5))
        self.assertEqual(50, get_fahrenheit(10))


#testing question c
    def test_get_random_number(self):
       results = [get_random_number() for _ in range(1000)]
       for number in results: 
        self.assertEqual(True, 1 <= number <= 5)


#testing question d
    def test_get_bonus_pay_amount(self):
       self.assertEqual(10, get_bonus_pay_amount(200))
       self.assertEqual(36, get_bonus_pay_amount(600))
       self.assertEqual(70, get_bonus_pay_amount(1000))
       self.assertEqual(120, get_bonus_pay_amount(1500))








