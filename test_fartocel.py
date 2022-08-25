import unittest
from fartocel import far_to_cel


class TestCelsToFar(unittest.TestCase):
    def test_cel(self):

        self.assertEqual(far_to_cel(32), 0.0)
        self.assertEqual(far_to_cel(5), -15.0)
        self.assertEqual(far_to_cel(104), 194.0)
        self.assertEqual(far_to_cel(-40), -40.0)

    def test_types(self):

        self.assertRaises(TypeError, far_to_cel, 5 + 2j)
        self.assertRaises(TypeError, far_to_cel, "five")
        self.assertRaises(TypeError, far_to_cel, [16, 22])
        self.assertRaises(TypeError, far_to_cel, True)
        self.assertRaises(TypeError, far_to_cel, [42])
