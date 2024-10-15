#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


#testing question a 
def test_get_sum_of_evens(self):
    self.assertEqual(30, test_get_sum_of_evens(11))
    self.assertEqual(30, test_get_sum_of_evens(10))
    self.assertEqual(8, test_get_sum_of_evens(20))


