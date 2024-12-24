"""
Файл для работы с базой данных.
"""
from __future__ import annotations

from typing import List
from venv import logger

from database.models import Bus


class BusHelper:
    """
    Вспомогательный класс, для CRUD-операций с таблицей Bus.
    """

    def __init__(self, session):
        self.session = session

    def create_bus(self, brand: str, state_number: str, capacity: int) -> Bus | bool:
        """
        Метод для создания объекта `автобус` в базе данных.
        :param brand: Марка автобуса
        :param state_number: Государственный номер автобуса.
        :param capacity: Вместимость автобуса
        :return: объект Bus или False, если невозможно создать объект.
        """
        db = self.session()
        new_bus = Bus(brand=brand, state_number=state_number, capacity=capacity)
        if not self.validate_bus(capacity):
            return False
        db.add(new_bus)
        db.commit()
        db.close()
        return new_bus

    def delete_bus(self, brand) -> bool:
        """
        Метод для удаления объекта `автобус` из базы данных.
        :param brand: Марка автобуса.
        :return: True, если автобус был успешно удален, False иначе.
        """
        db = self.session()
        bus = db.query(Bus).filter(Bus.brand == brand).first()
        if not bus:
            logger.error("There is no bus with brand %s", brand)
            return False
        db.delete(bus)
        db.commit()
        db.close()
        return True

    def get_all_buses(self) -> List[str]:
        """
        Метод для получения всех автобусов.
        :return: список с номерами всех добавленных в БД автобусов
        """
        db = self.session()
        buses = [bus.state_number for bus in db.query(Bus).all()]
        db.close()
        return buses

    @staticmethod
    def validate_bus(capacity) -> bool:
        """
        Валидация автобуса, перед добавлением в базу данных.
        :param capacity: Вместимость автобуса.
        :return: True, если валидация успешно пройдена, False иначе.
        """
        if capacity <= 0:
            logger.error("Capacity most be positive integer")
            return False
