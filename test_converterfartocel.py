import unittest
from converterfartocel import cel_to_far

class TestCelsToFar(unittest.TestCase):
    def test_far(self):

        self.assertEqual(cel_to_far(90), 194.0)
        self.assertEqual(cel_to_far(0), 32.0)
        self.assertEqual(cel_to_far(20), 68.0)
        self.assertEqual(cel_to_far(36.6), 97.88000000000001)
        self.assertEqual(cel_to_far(-20), -4)
    
    def test_types(self):


        self.assertRaises(TypeError, cel_to_far, 5+2j)
        self.assertRaises(TypeError, cel_to_far, "five")
        self.assertRaises(TypeError, cel_to_far, [16, 22])
        self.assertRaises(TypeError, cel_to_far, True)
        self.assertRaises(TypeError, cel_to_far, [42])
