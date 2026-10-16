import re
def find_hex_colors(text):
    # Поиск HEX-цветов в тексте
    pattern = r"#[0-9A-Fa-f]{6}\b"
    return re.findall(pattern, text)