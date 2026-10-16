# regex_checker.py
import re

def check_hex(text):
    # Простейшая проверка цвета
    pattern = r"^#[0-9A-Fa-f]{6}$"
    return bool(re.match(pattern, text))