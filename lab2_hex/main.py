from regex_checker import validate_hex_string, find_hex_in_file, find_hex_in_url, find_hex_in_text

def main():
    print("=== Утилита для работы с HEX-цветами ===")
    while True:
        print("\n1. Проверить строку\n2. Найти в тексте\n3. Найти в файле\n4. Найти по URL\n5. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == '1':
            s = input("Введите цвет: ")
            print("Корректно" if validate_hex_string(s) else "Ошибка")
        elif choice == '2':
            t = input("Введите текст: ")
            print(f"Найденные: {find_hex_in_text(t)}")
        elif choice == '3':
            p = input("Путь к файлу: ")
            print(f"Найденные: {find_hex_in_file(p)}")
        elif choice == '4':
            u = input("URL страницы: ")
            print(f"Найденные: {find_hex_in_url(u)}")
        elif choice == '5':
            break

if __name__ == "__main__":
