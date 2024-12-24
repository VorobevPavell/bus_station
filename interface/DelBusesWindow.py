"""
Окно удаления автобусов
"""


from venv import logger
from typing import List
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget

from core.bushelper import BusHelper
from database.connection import DatabaseConnection
from database.models import Bus
from dev.del_bus import Ui_DelBus


class DelBusesWindow(QWidget, Ui_DelBus, QWindow):
    session = DatabaseConnection.get_session()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(self.get_buses_from_db())
        self.delBusBtn.clicked.connect(self.del_bus_from_db)
        self.backBtn.clicked.connect(self.close)

    def del_bus_from_db(self):
        """
        Метод удаляет существующий автобус из базы данных.
        """
        state_number = self.comboBox.currentText()
        session = DatabaseConnection.get_session()
        db = session()
        bus_to_delete = db.query(Bus).filter(Bus.state_number == state_number).scalar()
        if not bus_to_delete:
            logger.error("there is no bus with %s state_number", state_number)
            return
        db.delete(bus_to_delete)
        db.commit()
        db.close()
        logger.debug("bus deleted from database. state_number: %s", state_number)

    def get_buses_from_db(self) -> List[str]:
        """
        Получает все автобусы из базы данных
        """
        bus_helpers = BusHelper(self.session)
        buses = bus_helpers.get_all_buses()
        return buses
