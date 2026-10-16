import re
class HexValidator:
    def __init__(self):
        self.pattern = re.compile(r"#[0-9A-Fa-f]{6}\b")

    def validate_text(self, text: str) -> list:
        return self.pattern.findall(text)

    def validate_file(self, filepath: str) -> list:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return self.validate_text(f.read())
        except FileNotFoundError:
            return []