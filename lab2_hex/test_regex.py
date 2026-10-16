# test_regex.py
import unittest
from regex_checker import HexValidator

class TestHexValidator(unittest.TestCase):
    def setUp(self):
        self.validator = HexValidator()

    def test_valid_hex(self):
        result = self.validator.validate_text("Цвета: #FF5733 и #000000")
        self.assertEqual(result, ["#FF5733", "#000000"])

    def test_invalid_hex(self):
        result = self.validator.validate_text("Неверный #12345")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()