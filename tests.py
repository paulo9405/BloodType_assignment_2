import unittest
from blood_type import *

class TestBloodTypeChecker(unittest.TestCase):

    def test_check_donors(self):
        expected_donors = ["A+", "A-", "O+", "O-"]
        self.assertEqual(compatibility_bloods["A+"]["donors"], expected_donors)

    def test_check_recipients(self):
        expected_recipients = ["A+", "AB+"]
        self.assertEqual(compatibility_bloods["A+"]["recipients"], expected_recipients)

    def test_invalid_blood_type(self):
        self.assertFalse(validate_blood("XZ"))

    def test_valid_blood_type(self):
        self.assertTrue(validate_blood("A+"))

    def test_invalid_menu_choice(self):
        self.assertFalse(validate_menu_choice("5"))

    def test_valid_menu_choice(self):
        self.assertTrue(validate_menu_choice("1"))

if __name__ == "__main__":
    unittest.main()