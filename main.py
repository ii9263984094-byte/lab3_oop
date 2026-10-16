"""Главный исполнительный модуль лабораторной работы."""

from models import Concert, TheaterPlay, Conference, Venue
from booking_system import BookingSystem
from exceptions import InvalidPriceError, EventNotFoundError, DataFormatError


def demo_exceptions() -> None:
    """Демонстрация обработки встроенных и пользовательских исключений."""
    print("--- 1. Тестирование работы исключений ---")

    # Собственное исключение: отрицательная цена
    try:
        Concert(1, "Тестовый концерт", -100.0, "Группа X")
    except InvalidPriceError as exc:
        print(f"[Поймано InvalidPriceError]: {exc}")

    # Встроенное исключение: деление на ноль
    try:
        result = 100 / 0
    except ZeroDivisionError as exc:
        print(f"[Поймано ZeroDivisionError]: {exc}")

    # Использование конструкции else и finally
    try:
        valid_price = float("1500")
    except ValueError:
        print("Ошибка приведении типа")
    else:
        print(f"[Успешно]: Стоимость преобразована без ошибок: {valid_price} руб.")
    finally:
        print("[finally]: Блок завершения вычислений выполнен всегда.")


def main() -> None:
    demo_exceptions()

    print("\n--- 2. Демонстрация работы CRUD и сохранения файлов ---")
    system = BookingSystem()

    # Create
    system.create_event(Concert(101, "Рок-Фестиваль", 2500.0, "Рок-Группа"))
    system.create_event(TheaterPlay(102, "Щелкунчик", 3000.0, "Большой Театр"))
    system.create_event(Conference(103, "DevOps Conf 2026", 0.0, "Облачные технологии"))

    system.venues.append(Venue(1, "Главный зал МГТУ", "2-я Бауманская ул., д. 5"))

    # Сохранение в файлы (JSON и XML)
    system.save_events_json("data_events.json")
    system.save_venues_xml("data_venues.xml")
    print("Данные успешно сохранены в файлы data_events.json и data_venues.xml")

    # Read / Загрузка из файлов
    loaded_system = BookingSystem()
    loaded_system.load_events_json("data_events.json")
    loaded_system.load_venues_xml("data_venues.xml")

    print("\nЗагруженные мероприятия:")
    for event in loaded_system.read_events():
        print("  -", event.get_info())

    # Update
    print("\nОбновление цены для ID 101...")
    loaded_system.update_event_price(101, 2800.0)
    print("Новая информация:", loaded_system.read_events()[0].get_info())

    # Delete
    print("\nУдаление мероприятия с ID 103...")
    loaded_system.delete_event(103)
    print("Оставшееся количество мероприятий:", len(loaded_system.read_events()))


if __name__ == "__main__":
    main()