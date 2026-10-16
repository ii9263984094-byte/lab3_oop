from regex_checker import HexValidator
def main():
    validator = HexValidator()
    print("=== Анализатор HEX-цветов ===")
    user_input = input("Введите текст с цветами: ")
    found = validator.validate_text(user_input)
    print(f"Найденные цвета: {found}")

if __name__ == "__main__":
    main()