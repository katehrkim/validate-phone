import unittest
from validate_phone import *

class ValidatePhoneTestCases(unittest.TestCase):
    """Tests for `validate_phone.py`."""

    def test_has_phone_number_true(self):
        """When you call has_phone_number() with a legitimate phone number, you should get true"""
        self.assertTrue(has_phone_number('my phone number: 111-222-3333'))

    def test_has_phone_number_false(self):
        """When you call has_phone_number() with a bad phone number, you should get false"""
        self.assertFalse(has_phone_number('please confirm your phone number: XXX-XXX-1234'))

    def test_get_phone_number(self):
        """When you call get_phone_number() with a good phone number, you should get the phone number"""
        self.assertEqual(get_phone_number("please don't share this: 999-888-1234"), '999-888-1234')

    def test_get_phone_number_none(self):
        """When you call get_phone_number() with a bad phone number, you should get None"""
        self.assertEqual(get_phone_number("please confirm your phone number: XXX-XXX-1234"), None)
    
    def test_get_all_phone_numbers(self):
        """When you call get_all_phone_numbers(), you get all the phone numbers back"""
        self.assertEqual(get_all_phone_numbers("234-609-1422, 350-802-0744, 123-603-8762"), ["234-609-1422", "350-802-0744", "123-603-8762"])
    
    def test_get_all_phone_numbers_but_no_numbers(self):
        """When you call get_all_phone_numbers() with no phone numbers, you get an empty array back"""
        self.assertEqual(get_all_phone_numbers("please confirm your phone number: XXX-XXX-1422"), [])

    def test_hide_phone_numbers(self):
        """When you call hide_phone_numbers(), it hides all the phone numbers"""
        self.assertEqual(hide_phone_numbers("234-620-1422, 350-830-0744, 123-603-8762"), 'XXX-XXX-1422, XXX-XXX-0744, XXX-XXX-8762')
    
    def test_format_phone_number(self):
        """When you call format_phone_number(), it formats all the phone numbers"""
        self.assertEqual(format_phone_number("(312) 454.9323, 3112223333, 350.820.0744, 123-630-8762"), '312-454-9323, 311-222-3333, 350-820-0744, 123-630-8762')

if __name__ == '__main__':
    unittest.main()