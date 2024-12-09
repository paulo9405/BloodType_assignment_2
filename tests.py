import unittest
from blood_type import *  # Import the functions and data from blood_type.py

# A class to test the blood type program
class TestBloodTypeChecker(unittest.TestCase):

    # Test if the donors for blood type "A+" are correct
    def test_check_donors(self):
        # The donors we expect for "A+"
        expected_donors = ["A+", "A-", "O+", "O-"]
        # Check if the actual donors match the expected donors
        self.assertEqual(compatibility_bloods["A+"]["donors"], expected_donors)

    # Test if the recipients for blood type "A+" are correct
    def test_check_recipients(self):
        # The recipients we expect for "A+"
        expected_recipients = ["A+", "AB+"]
        # Check if the actual recipients match the expected recipients
        self.assertEqual(compatibility_bloods["A+"]["recipients"], expected_recipients)

    # Test if the program catches an invalid blood type
    def test_invalid_blood_type(self):
        # "XZ" is not a valid blood type, so this should return False
        self.assertFalse(validate_blood("XZ"))

    # Test if the program accepts a valid blood type
    def test_valid_blood_type(self):
        # "A+" is a valid blood type, so this should return True
        self.assertTrue(validate_blood("A+"))

    # Test if the program catches an invalid menu choice
    def test_invalid_menu_choice(self):
        # "5" is not a valid menu option, so this should return False
        self.assertFalse(validate_menu_choice("5"))

    # Test if the program accepts a valid menu choice
    def test_valid_menu_choice(self):
        # "1" is a valid menu option, so this should return True
        self.assertTrue(validate_menu_choice("1"))

# Run the tests if this file is run directly
if __name__ == "__main__":
    unittest.main()
