"""
Файл для работы с базой данных.
"""
from __future__ import annotations

from typing import List
from venv import logger
from database.models import Station


class StationHelper:
    """
    Вспомогательный класс, для CRUD-операций с таблицей Route.
    """

    def __init__(self, session):
        self.session = session

    def create_station(self, name: str) -> Station:
        """
        Метод для создания объекта `станция` в базе данных.
        :param name: Имя, с которой создается станция
        :return: объект Station.
        """
        db = self.session()
        new_station = Station(name=name)
        db.add(new_station)
        db.commit()
        db.close()
        return new_station

    def delete_station(self, name: str) -> Station | bool:
        """
        Метод для удаления объекта `станция` из базы данных.
        :param name: Имя станции, которую нужно удалить.
        :return: True, если станция была успешна удалена, False иначе.
        """
        db = self.session()
        station = db.query(Station).filter(Station.name == name).first()
        if not station:
            logger.error("There is no station with name %s", name)
            return False
        db.delete(station)
        db.commit()
        db.close()
        return True

    def get_all_stations(self) -> List[str]:
        """
        Метод для получения всех станций.
        :return: список с названиями всех добавленных в БД станций
        """
        db = self.session()
        stations = [station.name for station in db.query(Station).all()]
        db.close()
        return stations
