import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertFalse(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Test"
        b = "fest"
        self.assertEqual(a, b, msg=" 'a' is not equal to 'b'  ")


if __name__ == '__main__ ':
    unittest.main(verbosity=2)
