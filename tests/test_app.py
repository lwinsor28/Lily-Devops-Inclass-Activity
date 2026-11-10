import unittest

from app import add_numbers


# Test add_numbers:
class TestAddition(unittest.TestCase):

    # Verify with two positive numbers
    def test_positive_numbers(self):
        actual_result = add_numbers(2, 3)
        self.assertEqual(actual_result, 5)

    # Verify with a negative number
    def test_negative_number(self):
        actual_result = add_numbers(-4, 6)
        self.assertEqual(actual_result, 2)


# Allow test file to run independently
if __name__ == "__main__":
    unittest.main()