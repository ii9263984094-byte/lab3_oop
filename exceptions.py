"""Модуль пользовательских исключений для системы бронирования билетов."""


class EventBookingError(Exception):
    """Базовое исключение для предметной области бронирования билетов."""


class InvalidPriceError(EventBookingError):
    """Исключение: указана некорректная (отрицательная) цена билета."""


class SeatAlreadyBookedError(EventBookingError):
    """Исключение: попытка повторно забронировать уже занятое место."""


class EventNotFoundError(EventBookingError):
    """Исключение: запрашиваемое мероприятие не найдено в базе."""


class DataFormatError(EventBookingError):
    """Исключение: ошибка формата при сериализации/десериализации JSON или XML."""