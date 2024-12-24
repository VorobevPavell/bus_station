"""
Файл для работы с базой данных.
"""
from __future__ import annotations

from datetime import datetime
from typing import List
from venv import logger

from database.models import Route, Station, Bus


class RouteHelper:
    """
    Вспомогательный класс, для CRUD-операций с таблицей Route.
    """

    def __init__(self, session):
        self.session = session

    def create_route(self, station: int, bus: int, dep_time: datetime) -> Route | bool:
        """
        Метод для создания объекта `рейс` в базе данных.
        :param station: id станции до которой выполняется рейс
        :param bus: id автобуса который выполняет рейс.
        :param dep_time: Время отправления
        :return: объект Route или False, если невозможно создать объект.
        """
        db = self.session()
        station_exist = db.query(Station).filter(Station.id == station).first()
        bus_exist = db.query(Bus).filter(Bus.id == bus).first()
        # создаем рейс только для существующих станций и автобусов
        if not station_exist or not bus_exist:
            logger.error("Cant create route to %s with %s bus", station, bus)
            return False
        new_route = Route(station_id=station, bus_id=bus, dep_time=dep_time)
        db.add(new_route)
        db.commit()
        db.close()
        return new_route

    def delete_route(self, route_id: int) -> bool:
        """
        Метод для удаления объекта `рейс` из базы данных.
        :param route_id: Уникальный номер рейса.
        :return: True, если рейс был успешно удален, False иначе.
        """
        db = self.session()
        route = db.query(Route).filter(Route.id == route_id).first()
        if not route:
            logger.error("There is no route with id %s", route_id)
            return False
        db.delete(route)
        db.commit()
        db.close()
        return True

    def get_all_routes(self) -> List[str]:
        """
        Метод для получения всех рейсов.
        :return: список с кодами всех рейсов
        """
        db = self.session()
        routes = [str(route.id) for route in db.query(Route).all()]
        db.close()
        return routes
