import re
def find_hex_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        pattern = r"#[0-9A-Fa-f]{6}\b"
        return re.findall(pattern, text)
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return []