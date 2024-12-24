"""
Окно удаления станции
"""


from venv import logger
from typing import List
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.stationhelper import StationHelper
from database.connection import DatabaseConnection
from database.models import Station
from dev.del_station import Ui_DelStation


class DelStationWindow(QWidget, Ui_DelStation, QWindow):
    session = DatabaseConnection.get_session()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(self.get_stations_from_db())
        self.delBusBtn.clicked.connect(self.del_station_from_db)
        self.backBtn.clicked.connect(self.close)

    def del_station_from_db(self):
        """
        Метод удаляет существующую станцию из базы данных.
        """
        name = self.comboBox.currentText()
        session = DatabaseConnection.get_session()
        db = session()
        station_to_delete = db.query(Station).filter(Station.name == name).scalar()
        if not station_to_delete:
            logger.error("there is no station with %s name", name)
            return
        db.delete(station_to_delete)
        db.commit()
        db.close()
        logger.debug("station deleted from database. name: %s", name)

    def get_stations_from_db(self) -> List[str]:
        """
        Получает все станции из базы данных
        """
        station_helper = StationHelper(self.session)
        stations = station_helper.get_all_stations()
        return stations
