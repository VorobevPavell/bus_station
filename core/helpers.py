"""
Вспомогательные функции бизнес-логики приложения.
"""
from __future__ import annotations

from sqlalchemy import func

from database.models import Station, Route, Bus


class Helpers:
    """
    Класс содержит основные методы для работы бизнес-логики.
    """

    def __init__(self, session):
        self.session = session

    def calculate_routes_to_station(self, station_name: str) -> int | None:
        """
        Метод рассчитывает количество рейсов до переданной станции.
        :param station_name: Имя станции до которой нужно рассчитать рейсы
        :return: Количество рейсов до указанной станции или None если указанной станции не существует
        """
        db = self.session()
        is_station_exist = (
            db.query(Station).filter(Station.name == station_name).first()
        )
        if not is_station_exist:
            return
        station_id = db.query(Station).filter(Station.name == station_name).first().id
        routes_to_station = (
            db.query(func.count(Route.id))
            .filter(Route.station_id == station_id)
            .scalar()
        )
        db.close()
        return routes_to_station

    def calculate_passengers(self):
        """
        Метот рассчитывает максимальное количество пассажиров, которое может обслужить автовокзал
        :return: Максимально возможное количество пассажиров.
        """
        db = self.session()
        total_capacity = db.query(func.sum(Bus.capacity)).scalar()
        db.close()
        return total_capacity
