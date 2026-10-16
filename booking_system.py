"""Модуль управляющего класса системы бронирования (CRUD + Persistence)."""

import json
import xml.etree.ElementTree as ET
from models import Event, Concert, TheaterPlay, Conference, Venue
from exceptions import EventNotFoundError, DataFormatError


class BookingSystem:
    """Главный сервис управления мероприятиями, площадками и файлами данных."""

    def __init__(self) -> None:
        self.events: list[Event] = []
        self.venues: list[Venue] = []

    # --- CRUD для Мероприятий ---
    def create_event(self, event: Event) -> None:
        """Create: добавление нового мероприятия в систему."""
        self.events.append(event)

    def read_events(self) -> list[Event]:
        """Read: получение списка всех мероприятий."""
        return self.events

    def update_event_price(self, event_id: int, new_price: float) -> None:
        """Update: обновление базовой стоимости мероприятия."""
        for event in self.events:
            if event.event_id == event_id:
                event.base_price = new_price
                return
        raise EventNotFoundError(f"Мероприятие с ID {event_id} не найдено в базе")

    def delete_event(self, event_id: int) -> None:
        """Delete: удаление мероприятия из системы."""
        initial_length = len(self.events)
        self.events = [e for e in self.events if e.event_id != event_id]
        if len(self.events) == initial_length:
            raise EventNotFoundError(f"Не удалось удалить: ID {event_id} отсутствует")

    # --- Работа с JSON ---
    def save_events_json(self, filepath: str) -> None:
        """Запись коллекции мероприятий в файл JSON."""
        data = [e.to_dict() for e in self.events]
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError as exc:
            raise DataFormatError(f"Ошибка записи в JSON-файл {filepath}: {exc}") from exc

    def load_events_json(self, filepath: str) -> None:
        """Чтение и восстанавливание объектов мероприятий из JSON."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.events.clear()
            for item in data:
                event_type = item.get("type")
                if event_type == "Concert":
                    obj = Concert(item["event_id"], item["title"], item["base_price"], item["performer"])
                elif event_type == "TheaterPlay":
                    obj = TheaterPlay(item["event_id"], item["title"], item["base_price"], item["director"])
                elif event_type == "Conference":
                    obj = Conference(item["event_id"], item["title"], item["base_price"], item["topic"])
                else:
                    continue
                self.events.append(obj)
        except (OSError, json.JSONDecodeError, KeyError) as exc:
            raise DataFormatError(f"Ошибка десериализации JSON {filepath}: {exc}") from exc

    # --- Работа с XML ---
    def save_venues_xml(self, filepath: str) -> None:
        """Запись площадок в файл XML."""
        root = ET.Element("venues")
        for venue in self.venues:
            root.append(venue.to_xml())
        tree = ET.ElementTree(root)
        try:
            tree.write(filepath, encoding="utf-8", xml_declaration=True)
        except OSError as exc:
            raise DataFormatError(f"Ошибка записи в XML-файл {filepath}: {exc}") from exc

    def load_venues_xml(self, filepath: str) -> None:
        """Чтение площадок из файла XML."""
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            self.venues = [Venue.from_xml(elem) for elem in root.findall("venue")]
        except (OSError, ET.ParseError) as exc:
            raise DataFormatError(f"Ошибка чтения XML-файла {filepath}: {exc}") from exc