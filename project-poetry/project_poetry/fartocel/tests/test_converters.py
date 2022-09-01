import unittest
from converters import cel_to_far


class TestCelsToFar(unittest.TestCase):
    def test_far(self):

        self.assertEqual(cel_to_far(90), 194.0)
        self.assertEqual(cel_to_far(0), 32.0)
        self.assertEqual(cel_to_far(20), 68.0)
        self.assertEqual(cel_to_far(36.6), 97.88)
        self.assertEqual(cel_to_far(-20), -4)
        self.assertEqual(cel_to_far(-273.15), -459.67)

        self.assertEqual(far_to_cel(32), 0.0)
        self.assertEqual(far_to_cel(5), -15.0)
        self.assertEqual(far_to_cel(194), 90.0)
        self.assertEqual(far_to_cel(-40), -40.0)

    def test_types(self):

        self.assertRaises(TypeError, cel_to_far, 5 + 2j)
        self.assertRaises(TypeError, cel_to_far, "five")
        self.assertRaises(TypeError, cel_to_far, [16, 22])
        self.assertRaises(TypeError, cel_to_far, True)
        self.assertRaises(TypeError, cel_to_far, [42])

        self.assertRaises(TypeError, far_to_cel, 5 + 2j)
        self.assertRaises(TypeError, far_to_cel, "five")
        self.assertRaises(TypeError, far_to_cel, [16, 22])
        self.assertRaises(TypeError, far_to_cel, True)
        self.assertRaises(TypeError, far_to_cel, [42])
