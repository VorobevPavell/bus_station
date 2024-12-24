"""
Окно добавления станций
"""


from venv import logger

from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from database.connection import DatabaseConnection
from database.models import Station
from dev.add_station import Ui_Station


class AddStationWindow(QWidget, Ui_Station, QWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addStationBtn.clicked.connect(self.add_station_into_db)
        self.backBtn.clicked.connect(self.close)

    def add_station_into_db(self):
        """
        Метод добавляет новую станцию в базу данных.
        """
        name = self.name.text()
        session = DatabaseConnection.get_session()
        db = session()
        if db.query(Station).filter(Station.name == name).scalar():
            logger.error("station already exists with %s name", name)
            return
        new_station = Station(name=name)
        db.add(new_station)
        db.commit()
        db.close()
        logger.debug("station added to database. name: %s", name)
