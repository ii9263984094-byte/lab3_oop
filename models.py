"""Модуль основных классов предметной области (Вариант 10)."""

import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Any
from exceptions import InvalidPriceError, DataFormatError


class Event(ABC):
    """Абстрактный класс мероприятия."""

    def __init__(self, event_id: int, title: str, base_price: float) -> None:
        if base_price < 0:
            raise InvalidPriceError(f"Цена не может быть отрицательной: {base_price}")
        self.event_id: int = event_id
        self.title: str = title
        self.base_price: float = base_price

    @abstractmethod
    def get_info(self) -> str:
        """Абстрактный метод получения подробной информации о мероприятии."""

    def to_dict(self) -> dict[str, Any]:
        """Сериализация данных объекта в словарь для сохранения в JSON."""
        return {
            "type": self.__class__.__name__,
            "event_id": self.event_id,
            "title": self.title,
            "base_price": self.base_price,
        }


class Concert(Event):
    """Класс Концерт."""

    def __init__(self, event_id: int, title: str, base_price: float, performer: str) -> None:
        super().__init__(event_id, title, base_price)
        self.performer: str = performer

    def get_info(self) -> str:
        return f"Концерт: «{self.title}» | Исполнитель: {self.performer} | Цена: {self.base_price} руб."

    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data["performer"] = self.performer
        return data


class TheaterPlay(Event):
    """Класс Спектакль."""

    def __init__(self, event_id: int, title: str, base_price: float, director: str) -> None:
        super().__init__(event_id, title, base_price)
        self.director: str = director

    def get_info(self) -> str:
        return f"Спектакль: «{self.title}» | Режиссер: {self.director} | Цена: {self.base_price} руб."

    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data["director"] = self.director
        return data


class Conference(Event):
    """Класс Конференция."""

    def __init__(self, event_id: int, title: str, base_price: float, topic: str) -> None:
        super().__init__(event_id, title, base_price)
        self.topic: str = topic

    def get_info(self) -> str:
        return f"Конференция: «{self.title}» | Тема: {self.topic} | Цена: {self.base_price} руб."

    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data["topic"] = self.topic
        return data


class Venue:
    """Площадка проведения мероприятий (для сохранения в XML)."""

    def __init__(self, venue_id: int, name: str, address: str) -> None:
        self.venue_id: int = venue_id
        self.name: str = name
        self.address: str = address

    def to_xml(self) -> ET.Element:
        """Сериализация объекта Площадки в элемент XML."""
        elem = ET.Element("venue")
        ET.SubElement(elem, "id").text = str(self.venue_id)
        ET.SubElement(elem, "name").text = self.name
        ET.SubElement(elem, "address").text = self.address
        return elem

    @classmethod
    def from_xml(cls, elem: ET.Element) -> "Venue":
        """Десериализация объекта Площадки из элемента XML."""
        try:
            return cls(
                venue_id=int(elem.findtext("id", "0")),
                name=elem.findtext("name", ""),
                address=elem.findtext("address", ""),
            )
        except (ValueError, TypeError) as exc:
            raise DataFormatError(f"Ошибка чтения данных XML площадки: {exc}") from exc


class Seat:
    """Место в зрительном зале."""

    def __init__(self, row: int, number: int) -> None:
        self.row: int = row
        self.number: int = number
        self.is_booked: bool = False


class User:
    """Пользователь системы бронирования."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        self.user_id: int = user_id
        self.name: str = name
        self.email: str = email


class Ticket:
    """Билет на мероприятие."""

    def __init__(self, ticket_id: int, event: Event, seat: Seat) -> None:
        self.ticket_id: int = ticket_id
        self.event: Event = event
        self.seat: Seat = seat


class Booking:
    """Заказ на бронирование."""

    def __init__(self, booking_id: int, user: User, ticket: Ticket) -> None:
        self.booking_id: int = booking_id
        self.user: User = user
        self.ticket: Ticket = ticket


class Payment:
    """Платежная транзакция."""

    def __init__(self, payment_id: int, amount: float, status: str = "Completed") -> None:
        self.payment_id: int = payment_id
        self.amount: float = amount
        self.status: str = status