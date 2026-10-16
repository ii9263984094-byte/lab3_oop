import re
import requests

HEX_SEARCH_PATTERN = r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
FULL_HEX_PATTERN = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'

def validate_hex_string(color_str: str) -> bool:
    return bool(re.match(FULL_HEX_PATTERN, color_str))

def find_hex_in_text(text: str) -> list:
    return re.findall(HEX_SEARCH_PATTERN, text)

def find_hex_in_file(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return find_hex_in_text(f.read())
    except FileNotFoundError:
        return []

def find_hex_in_url(url: str) -> list:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return find_hex_in_text(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        return []