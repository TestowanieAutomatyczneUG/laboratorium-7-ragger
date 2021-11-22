import unittest

from ValidPassword import ValidPassword


class TestValidPassword(unittest.TestCase):
    def setUp(self):
        self.validPassword = ValidPassword()

    def tearDown(self):
        self.validPassword = None

    def test_valid_empty(self):
        self.assertFalse(self.validPassword.password(""))

    def test_valid_not_8_lenght_long(self):
        self.assertFalse(self.validPassword.password("A@1x"))

    def test_valid_8_numbers(self):
        self.assertFalse(self.validPassword.password("123456789"))

    def test_vvalid_uppercase_8_letters_number_special_case(self):
        self.assertTrue(self.validPassword.password("Abcdefgh1!"))

    def test_valid_3_uppercase_5_loweecase_number_special(self):
        self.assertTrue(self.validPassword.password("AlaMaKot9@"))
    def test_valid_array(self):
        self.assertRaises(Exception, self.validPassword.password, [])

    def test_valid_object(self):
        self.assertRaises(Exception, self.validPassword.password, {})
    def test_valid_not_a_string(self):
        self.assertRaises(Exception, self.validPassword.password, 12)

    def test_valid_None(self):
        self.assertRaises(Exception, self.validPassword.password, None)
    def test_valid_False(self):
        self.assertRaises(Exception, self.validPassword.password, False)

