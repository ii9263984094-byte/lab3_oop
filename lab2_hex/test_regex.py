import unittest
from regex_checker import validate_hex_string, find_hex_in_text

class TestHexChecker(unittest.TestCase):

    def test_valid_hex(self):
        self.assertTrue(validate_hex_string("#FFF"))
        self.assertTrue(validate_hex_string("#123456"))

    def test_invalid_hex(self):
        self.assertFalse(validate_hex_string("123456"))
        self.assertFalse(validate_hex_string("#GGGGGG"))

    def test_find_in_text(self):
        text = "Цвета #ff5733 и #000, плохой код #1234G."
        found = find_hex_in_text(text)
        self.assertIn("ff5733", found)
        self.assertIn("000", found)
        self.assertNotIn("1234G", found)


if __name__ == '__main__':
    unittest.main()