"""
Окно добавления рейсов
"""
from dateutil import parser
from venv import logger

from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.bushelper import BusHelper
from core.stationhelper import StationHelper
from database.connection import DatabaseConnection
from database.models import Route
from dev.add_route import Ui_Route


class AddRouteWindow(QWidget, Ui_Route, QWindow):
    def __init__(self):
        session = DatabaseConnection.get_session()
        super().__init__()
        self.setupUi(self)
        self.station_helper = StationHelper(session)
        self.buses_helper = BusHelper(session)
        self.stations.addItems(self.station_helper.get_all_stations())
        self.buses.addItems(self.buses_helper.get_all_buses())
        self.addRouteBtn.clicked.connect(self.add_route_into_db)
        self.backBtn.clicked.connect(self.close)

    def add_route_into_db(self):
        """
        Метод добавляет новый рейс в базу данных.
        :return:
        """
        station = self.stations.currentText()
        bus = self.buses.currentText()
        dep_time = self.dateTimeEdit.text()
        parsed_date = parser.parse(dep_time)
        session = DatabaseConnection.get_session()
        db = session()
        if (
            db.query(Route)
            .filter(
                Route.station_id == station
                and Route.bus_id == bus
                and Route.dep_time == parsed_date
            )
            .scalar()
        ):
            logger.error(
                "route to %s on %s bus already exists at %s", station, bus, parsed_date
            )
            return
        new_route = Route(station_id=station, bus_id=bus, dep_time=parsed_date)
        db.add(new_route)
        db.commit()
        db.close()
        logger.debug(
            "route added to database. station: %s bus: %s dep_time: %s",
            station,
            bus,
            parsed_date,
        )
